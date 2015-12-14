# Python und Orchstra Webservices

Bei der Installation von Python, add to PATH Variable und install pip anclicken.

## Installation von suds

    pip install suds-jurko


## Deployment Services

    (Port1)
        Methods (17):
            activateScenario(scenarioID scenarioID, token token)
            aquireDeploymentToken()
            deActivateScenario(scenarioID scenarioID, token token)
            deployScenarioCallback(token token, xs:base64Binary serializedScenario, xs:string comment)
            freeDeploymentToken(token token)
            getAllDeployedScenarios()
            getDeployedScenarios(xs:string userID)
            getDeploymentInfo(token token)
            getScenarioFile(scenarioID scenarioID, xs:string verstionTag)
            getScenarioHistory(scenarioIdentifier scenarioIdentifier)
            getScenarioInfo(scenarioID scenarioID)
            reDeployScenarioCallback(token token, xs:base64Binary serializedScenario, xs:string comment)
            resumeAllScenarios(token token, xs:integer mode)
            resumeScenario(scenarioID scenarioID, xs:integer mode)
            suspendAllScenarios(token token, xs:integer mode)
            suspendScenario(scenarioID scenarioID, xs:integer mode)
            unDeployScenarioCallback(token token, uniqueScenarioID uniqueScenarioID)
        Types (0):
		
## Other Services