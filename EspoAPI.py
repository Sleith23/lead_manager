from espo_api_client import EspoAPI
import requests
client = EspoAPI('https://gps.espocloud.com/', '8d74f4c20462b7d9ab0bba90087997fe')

# response = client.request("GET", "Lead")
# print(response)
# print("Leads found:", len(response))

# Create a lead
data = {
    'firstName': 'John',
    'lastName': 'Does',
    'phoneNumber': '+11111-22222-33333',
    'source': 'Web Site',
    'assignedUserId': '1',
    'industry': 'Legal',
}
# print(client.request('POST', 'Lead', data))

# # Update
# print(client.request('PUT', 'Lead/5b3c37b74b19680f1', {'lastName': 'Alice'}))

# # Get accounts

leads = client.request("GET", "Lead", params={"maxSize": 1})
print(leads)

#Get accounts with search params
#params = {
#     "select": "id,phoneNumber",
#     "where": [
#         {
#             "type": "equals",
#             "attribute": "industry",
#             "value": 'Cannabis',
#         },
#     ],
# }
# print(client.request('GET', 'Account', params))

# # Delete an opportunity
# print(client.request('DELETE', 'Opportunity/5b3b0b8c0b2b8bea5'))

