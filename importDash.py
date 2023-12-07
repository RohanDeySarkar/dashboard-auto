import requests
import json

# Dashboard ID
url = "http://127.0.0.1:5601/api/kibana/dashboards/export?dashboard=c91f1440-1087-11ed-acb3-f187705f8cec"

res = requests.get(url)
data = res.json()

with open('savedObject.json', 'w') as f:
	json.dump(data, f)


print(data)