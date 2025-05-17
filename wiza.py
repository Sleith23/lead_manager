# -*- coding: utf-8 -*-
"""
Created on Fri May 16 21:51:38 2025

@author: scott
"""
import json
import http.client

api_key = "8a50ddeaf6922d49e1026f5fdf8671b5e4fa579bbfee81ee68526df8f1bbdab1" # update with your api_key
list_id = 3658586 # update with the id of the list that you would like returned

conn = http.client.HTTPSConnection('wiza.co')
authorization = ("Bearer {api_key}").format(api_key=api_key)
payload = ''
headers = { 'Authorization': authorization }
url = ("/api/lists/{list_id}/contacts?segment=people").format(list_id=list_id)
conn.request('GET', url, payload, headers)
res = conn.getresponse()
data = res.read()
#print(data.decode('utf-8'))

response = json.loads(data.decode('utf-8'))
contacts = response.get('data',[])

# for contact in contacts:
#     print("Full Name:", contact.get("full_name"))
#     print("Email:", contact.get("email"))
#     print("Title:", contact.get("title"))
#     print("Company:", contact.get("company"))
#     print("Work Phone:", contact.get("phone_number1"))
#     print("Mobile Phone:", contact.get("mobile_phone1"))

contact = response['data'][0]
phone = contact.get("phone_number1")
firstName = contact.get("first_name")
lastName = contact.get("last_name")
email = contact.get("email")
account = contact.get("company")

print(firstName)
print(lastName)
print(email)
print(account)
print(phone)


from espo_api_client import EspoAPI
import requests
client = EspoAPI('https://gps.espocloud.com/', '8d74f4c20462b7d9ab0bba90087997fe')

# response = client.request("GET", "Lead")
# print(response)
# print("Leads found:", len(response))

# Create a lead
data = {
    'firstName': firstName,
    'lastName': lastName,
    'phoneNumber': phone,
    'industry': 'Cannabis',
}
print(client.request('POST', 'Lead', data))

# # Update
# print(client.request('PUT', 'Lead/5b3c37b74b19680f1', {'lastName': 'Alice'}))

# # Get accounts

leads = client.request("GET", "Lead", params={"firstName": 'Luke'})
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


