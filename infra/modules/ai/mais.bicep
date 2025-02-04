@description('Azure region of the deployment')
param location string

@description('Tags to add to the resources')
param tags object

@description('Name of the AI service')
param aiServiceName string

@allowed([
  'S0'
])
@description('AI service SKU')
param aiServiceSkuName string = 'S0'

var aiServiceNameCleaned = replace(aiServiceName, '-', '')

resource aiServices 'Microsoft.CognitiveServices/accounts@2023-05-01' = {
  name: aiServiceNameCleaned
  location: location
  sku: {
    name: aiServiceSkuName
  }
  kind: 'CognitiveServices'
  properties: {
    publicNetworkAccess: 'Enabled'
    disableLocalAuth: false
    apiProperties: {
      statisticsEnabled: false
    }
    customSubDomainName: aiServiceNameCleaned
  }
  identity: {
    type: 'SystemAssigned'
  }
  tags: tags
}

var maisKey = aiServices.listKeys()

output aiServicesId string = aiServices.id
output aiServicesEndpoint string = aiServices.properties.endpoint
output aiServicesName string = aiServices.name
output aiServicesPrincipalId string = aiServices.identity.principalId
output aiServicesPrimaryKey string = maisKey.key1
