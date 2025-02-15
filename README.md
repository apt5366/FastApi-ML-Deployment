# FastAPI ML Deployment 🚀
This project deploys an ML model using FastAPI, Docker, and Kubernetes.

## 🔹 Features
- Containerized with **Docker**
- Deployed on **Kubernetes (Minikube)**
- REST API tested with **Postman**
- Model trained using **Scikit-Learn**

(Thisngs to remember, for Minikube to run, need to disable firewall on McCafee AntiVirus)

## 🔹 Setup
```bash
git clone https://github.com/your-username/fastapi-ml-deployment.git
cd fastapi-ml-deployment
docker build -t fastapi-ml .
minikube start
kubectl apply -f deployment.yaml
