from fastapi import FastAPI
import joblib
import numpy as np

model = joblib.load('app/iris_model.joblib')

class_names= np.array(['setosa', 'versicolor', 'virginica'])

app=FastAPI()   

@app.get('/')
def reed_root():
    return {'message':'Iris Model API'}

@app.post('/predict')
def predict(data:dict):
    features = np.array(data['features']).reshape(1,-1)
    prediction = model.predict(features)
    class_name = class_names[prediction][0]
    return {'prediction':class_name}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


