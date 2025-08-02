# -*- coding: utf-8 -*-
"""
Created on Fri May 16 21:51:38 2025

@author: scot
"""
import json
import http.client
import constants
api_key = constants.wiza_api_key # update with your api_key
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
crm_leads=[]
    
from espo_api_client import EspoAPI, EspoAPIError
import requests
client = EspoAPI(constants.espo_api_url, constants.espo_api_key)


for contact in contacts:
    phone = contact.get("phone_number1")
    firstName = contact.get("first_name")
    lastName = contact.get("last_name")
    email = contact.get("email")
    account = contact.get("company")
    title = contact.get("title")
    linkedin = contact.get("linkedin")
    state = contact.get("company_region")
    website = f"www.{contact.get('domain', '')}"

    

    lead_data = {
        'firstName': firstName,
        'lastName': lastName,
        'phoneNumber': phone,
        'emailAddress': email,
        'industry': 'healthcare',
        'accountName': account,
        'title' : title,
        'website' : website,
        'cLinkedin' : linkedin,
        'addressState' : state,
        
    }
    
    crm_leads.append(lead_data)
for lead in crm_leads:
    print(lead)
for lead in crm_leads:
    try:
        print("Attempting to create lead:", lead['emailAddress'])
        client.request('POST', 'Lead', lead)
        print("Lead created:", lead['emailAddress'])

    except EspoAPIError as e:
        if client.status_code == 409:
            print("Duplicate lead skipped:", lead['emailAddress'])
            continue  # Skip to next
        else:
            print("EspoAPIError:", str(e))
            continue  # Optional: keep going despite other errors

    except Exception as e:
        print("Unexpected error:", str(e))
        continue  # Continue loop despite failure

    
    
    
# response = client.request("GET", "Lead")
# print(response)
# print("Leads found:", len(response))

# Create a lead
# data = {
#     'firstName': firstName,
#     'lastName': lastName,
#     'phoneNumber': phone,
#     'industry': '',
#     'emailAddress' : email
# }

#Create Lead
#client.request('POST', 'Lead', data)

# # Update
#client.request('PUT', 'Lead/6828b1cd46887a666', {'emailAddress': email})


# # Get accounts

#leads = client.request("GET", "Lead", params={"maxSize": 1})
#print(leads)

#Get accounts with search params
# params = {
#     "select": "id,phoneNumber,name",
#     "where": [
#         {
#             "type": "equals",
#             "attribute": "industry",
#             "value": '',
#         },
#     ],
# }
# #print(client.request('GET', 'Lead', params)
# response = client.request('GET', 'Lead', params)
# first_lead = response['list'][0]
#print(first_lead)
# # Delete an opportunity
# print(client.request('DELETE', 'Opportunity/5b3b0b8c0b2b8bea5'))


