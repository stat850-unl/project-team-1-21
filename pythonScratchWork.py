import requests
import json
import pandas as pd
from skimpy import skim
import matplotlib.pyplot as plt

#addnot

# API KEY
api_key = 'RucYMPTp3yg6yYY0ktOEnbxaFDNvsDXDIQfGV3NK'

#API URL
apiUrl = "https://api.eia.gov/v2/electricity/electric-power-operational-data/data/?frequency=monthly&data[0]=ash-content&data[1]=consumption-for-eg&data[2]=consumption-for-eg-btu&data[3]=consumption-uto&data[4]=consumption-uto-btu&data[5]=cost&data[6]=cost-per-btu&data[7]=generation&data[8]=heat-content&data[9]=receipts&data[10]=receipts-btu&data[11]=stocks&data[12]=sulfur-content&data[13]=total-consumption&data[14]=total-consumption-btu&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000"

#Combined API URL and API key, will be used as a single input inton the api function
urlAndKey = f"{apiUrl}&api_key={api_key}"

# HEADER, an input to the api
headers = {
  "X-Params": json.dumps({
        "frequency": "monthly",
        "data": [
            "ash-content",
            "consumption-for-eg",
            "consumption-for-eg-btu",
            "consumption-uto",
            "consumption-uto-btu",
            "cost",
            "cost-per-btu",
            "generation",
            "heat-content",
            "receipts",
            "receipts-btu",
            "stocks",
            "sulfur-content",
            "total-consumption",
            "total-consumption-btu"
            ],
        "facets": {},
        "start": None,
        "end": None,
        "sort": [
            {
                "column": "period",
                "direction": "desc"
            }
        ],
        "offset": 0,
        "length": 5000 #ADJUSTABLE; WILL EXTEND WHEN I GET MORE SPACE MY COMPUTER IS MELTING
        })
  }

# GET REQUEST, as stated in the EIA method section
response = requests.get(urlAndKey, headers=headers)

# Response Status code (200 = success)
if response.status_code == 200:
    data = response.json()  # read response
else:
    print(f"REQUEST FAILED---CODE: {response.status_code}")
    print(response.text)



df1=pd.DataFrame(data)
df1=pd.DataFrame(data['response']['data'])
df1.head()
skim(df1)


pd.set_option('display.max_columns',40)
df1.groupby('fuelTypeDescription').count()

dfash=df1.groupby('fuelTypeDescription')['ash-content'].mean()
dfsulfur=df1.groupby('fuelTypeDescription')['sulfur-content'].mean()
dfash.plot(kind='bar')
plt.show()
plt.close()
dfsulfur.plot(kind='bar')
plt.show()
plt.close()
dfsulfur
dfash

plt.close('all')
df1['cost-per-btu']

dfcost=df1.groupby('fuelTypeDescription')['cost-per-btu'].mean()
dfcost.plot(kind='bar')
plt.show()
dfcost
