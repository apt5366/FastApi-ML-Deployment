import json
import requests

data= {'features':[1, 2, 3, 4]}

url = 'http://localhost:8000/predict'

predictions=[]
for record in data:
    payload= {'features':record}
    payload = json.dumps(payload)
    response = requests.post(url, data= payload)  
    predictions.append(response.json()['prediction'])

print(predictions) 
# data = json.dumps(data)
# response = requests.post(url, data) 
# print(response.json())