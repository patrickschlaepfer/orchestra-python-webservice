from suds.client import Client
from suds.sudsobject import asdict

import sys
import base64
import configparser
import logging

# Usage: py deploy_scenario.py <ScenarioName> <Deployment-Kommentar> <PfadZuPSC> <Instanz>

logging.basicConfig(level=logging.INFO)

config = configparser.ConfigParser()
config.read('servers.ini')

deployScenario = str(sys.argv[1])
deploymentComment = str(sys.argv[2])
pscFile = str(sys.argv[3])
instance = str(sys.argv[4])

hostconfig = config[instance]
host = hostconfig['Host']
port = hostconfig['Port']
user = hostconfig['User']
passwd = hostconfig['Password']
protocol = hostconfig['Protocol']
deployService = hostconfig['DeploymentService']

wsdlurl = protocol+'://'+host+':'+port+deployService

# print (deployScenario)

# data = open(pscFile, "rb").read()
# encoded_psc = base64.encodestring(data)

with open(pscFile, "rb") as psc_file:
  	encoded_psc = base64.b64encode(psc_file.read()).decode()
		
# print (encoded_psc)

client = Client(wsdlurl, username=user, password=passwd, timeout=180)

# prints all available methods and types
# print (client)

allDeployedScenarios = client.service.getAllDeployedScenarios()

# Accuire a token
deploymentToken = client.service.aquireDeploymentToken()

# loop thru the results
for item in allDeployedScenarios:
	if(item.name == deployScenario):
		print (item.name)
		scenarioID = item.scenarioID
		
		scenarioInfo = client.service.getScenarioInfo(scenarioID)
		
		# Deactivate Scenario
		deActivateResponse = client.service.deActivateScenario(scenarioID, deploymentToken)
		
		# Redeploy as it's already deployed
		try:
			reDeployScenarioCallback = client.service.reDeployScenarioCallback(deploymentToken, encoded_psc, deploymentComment)
		except (HTTPError, URLError) as error:
			logging.error('Data error')
		except timeout:
			logging.error('socket time out')
		else:
			logging.info('Access successful')
		
		# re-Activate scenario
		activateScenario = client.service.activateScenario(scenarioID, deploymentToken)
		
		getDeploymentInfo = client.service.getDeploymentInfo(deploymentToken);
		print (getDeploymentInfo)
		
# Release deployment token
client.service.freeDeploymentToken(deploymentToken)
	
	