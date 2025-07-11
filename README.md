# Ballon d'Or Voting App 

This is a full voting application deployed on Kubernetes using Flask, Redis, and Docker.  
It allows users to vote for their favorite Ballon d'Or candidate and view the live results.

---

##  Features

- Vote for top football players (e.g., Mohamed Salah, Dembélé, Yamal, Raphinha, Pedri, Mbappé).
- Votes are stored in Redis and displayed in real-time.
- Deployed using Kubernetes with proper deployments and services.
- External access using `ngrok`.

---

##  Technologies Used

- Python (Flask)
- Redis
- Docker
- Kubernetes
- ngrok (for external access)

---

##  Project Structure

```text
.
├── app.py                   # Vote app backend
├── result_app.py            # Result app backend (custom)
├── Dockerfile               # Dockerfile for both apps (one at a time)
├── vote-deployment.yaml     # Kubernetes deployment for vote-app
├── vote-service.yaml        # Kubernetes service for vote-app
├── result-deployment.yaml   # Kubernetes deployment for result-app
├── result-service.yaml      # Kubernetes service for result-app
├── redis-deployment.yaml    # Redis deployment
├── redis-service.yaml       # Redis service
├── postgres-deployment.yaml # Postgres (used by worker)
├── postgres-service.yaml    # Postgres service
├── worker-deployment.yaml   # Worker to sync Redis → Postgres
├── namespace.yaml
├── resource-quota.yaml


How to Run:
1. Start Minikube
minikube start

2. Apply all manifests

kubectl apply -f namespace.yaml
kubectl apply -f resource-quota.yaml
kubectl apply -f redis-deployment.yaml
kubectl apply -f redis-service.yaml
kubectl apply -f postgres-deployment.yaml
kubectl apply -f postgres-service.yaml
kubectl apply -f vote-deployment.yaml
kubectl apply -f vote-service.yaml
kubectl apply -f worker-deployment.yaml
kubectl apply -f result-deployment.yaml
kubectl apply -f result-service.yaml

External Access with ngrok
First, make sure you have ngrok and your authtoken configured
Get your Minikube IP:
minikube ip
Start tunnels:
ngrok http <minikube_ip>:31000   # Vote app
ngrok http <minikube_ip>:31001   # Result app

