#
# Credentials: webservice, web123
from suds.client import Client
from suds.sudsobject import asdict
from properties import *

client = Client(wsdlurl, username=user, password=passwd)

result = client.service.getCumulatedInfo() 

print (result[0])

print (result[0].runningProcesses)

# loop thru the results
for item in result:
	print (item.scenarioName)
	
	