# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "d0cf6c60-5574-4282-bac5-e35a2b030bfd",
# META       "default_lakehouse_name": "sample",
# META       "default_lakehouse_workspace_id": "e45e058c-5aaa-4a3e-a690-b7759705bf4b",
# META       "known_lakehouses": [
# META         {
# META           "id": "d0cf6c60-5574-4282-bac5-e35a2b030bfd"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

import requests

# 1. Get the current context IDs
workspace_id = mssparkutils.runtime.context.get("currentWorkspaceId")
lakehouse_name = "sample"

# 2. Get the Lakehouse ID from the name (if you don't already have the GUID)
lh_info = mssparkutils.lakehouse.get(lakehouse_name)
lakehouse_id = lh_info['id']

# 3. Call the Fabric REST API using the notebook's internal token
token = mssparkutils.credentials.getToken("pbi") # 'pbi' stands for Power BI/Fabric
headers = {"Authorization": f"Bearer {token}"}
url = f"https://api.fabric.microsoft.com/v1/workspaces/{workspace_id}/lakehouses/{lakehouse_id}"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    # Safely navigate the dictionary
    properties = data.get('properties', {})
    sql_props = properties.get('sqlEndpointProperties', {})
    connection_string = sql_props.get('connectionString')
    
    if connection_string:
        print(f"Success! SQL Endpoint: {connection_string}")
    else:
        print("Lakehouse found, but SQL Endpoint is not provisioned yet.")
else:
    print(f"Failed to get data. Status: {response.status_code}")
    print(response.text)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import requests

# 1. Try to get IDs from context
workspace_id = mssparkutils.runtime.context.get("currentWorkspaceId")
lakehouse_id = mssparkutils.runtime.context.get("currentLakehouseId")

# FALLBACK: If currentLakehouseId is missing, try to get the pinned/default one
if not lakehouse_id:
    try:
        # This looks for the lakehouse you see in the left-hand pane
        default_lakehouse = mssparkutils.lakehouse.get("sample") # replace "sample" with your lh name if needed
        lakehouse_id = default_lakehouse.get('id')
    except:
        pass

if not lakehouse_id:
    print("❌ Error: Could not detect a Lakehouse ID. Make sure a Lakehouse is added to the notebook.")
else:
    # 2. Get Token
    try:
        token = mssparkutils.credentials.getToken("pbi")
        headers = {"Authorization": f"Bearer {token}"}
        
        # 3. API Call
        url = f"https://api.fabric.microsoft.com/v1/workspaces/{workspace_id}/lakehouses/{lakehouse_id}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            # The API response structure for the connection string
            props = data.get('properties', {})
            sql_props = props.get('sqlEndpointProperties', {})
            sql_endpoint = sql_props.get('connectionString')
            
            if sql_endpoint:
                print(f"✅ Lakehouse Name: {data.get('displayName')}")
                print(f"🔗 SQL Endpoint: {sql_endpoint}")
            else:
                print("⚠️ Lakehouse found, but SQL Endpoint is still provisioning or unavailable.")
        else:
            print(f"❌ API Error {response.status_code}: {response.text}")
            
    except Exception as e:
        print(f"❌ Authentication Error: {str(e)}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
