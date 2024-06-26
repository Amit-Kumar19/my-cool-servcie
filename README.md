# My Cool Service

## Overview
This project implements a REST API with two endpoints using Flask:
1. `GET /api/users` - Retrieves a list of users. Only authenticated users can access this endpoint.
2. `POST /api/users` - Creates a new user. Only users with the "admin" role can access this endpoint.

Authorization is managed by Open Policy Agent (OPA). Both the API service and OPA run in a Kubernetes cluster.

## Prerequisites
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [Docker](https://docs.docker.com/get-docker/)

## Project Structure
```bash
├── app # Main application directory
│ ├── __init__.py  # Flask application setup
│ ├── auth.py  # Authentication and token verification
│ └── config.py  # Authentication and token verification
│ └── main.py  # Authentication and token verification
│ └── utils.py  # Utility functions (e.g., logging)
├── kubernetes
│ ├── flask-deployment.yaml  # Kubernetes deployment configuration for Flask app
│ ├── flask-service.yaml  # Kubernetes service configuration for Flask app
│ └── opa-configmap.yaml  # OPA policy ConfigMap
│ └── opa-deployment.yaml # Kubernetes deployment configuration for OPA
├── policy
│ ├── policy.rego # OPA policy file 
├── tests
│ └── test_app.py # Unit tests for the application
├── .gitignore 
├── Dockerfile # Dockerfile to build the application image
└── README.md # This README file
├── requirements.txt # Python dependencies
├── run.py #Entry point for running the Flask app
```

## Setup

### 1. Start Minikube
To start Minikube, run the following commands:
```sh
minikube start
```

### 2. Build Docker Images

```shell
eval $(minikube docker-env)
docker build -t my-cool-service:latest .
```

### 3. Deploy the Application to Kubernetes
Deploy the application and OPA to the Kubernetes cluster using the provided manifests:

```shell
kubectl apply -f kubernetes/flask-deployment.yaml
kubectl apply -f kubernetes/flask-service.yaml
kubectl apply -f kubernetes/opa-configmap.yaml
kubectl apply -f kubernetes/opa-deployment.yaml
```

### 4. Start the Flask service:
```
minikube service flask-service
```

### 5. Test the Application
GET /api/users <br/>
To test the GET /api/users endpoint, run:<br/>
```shell
curl -H "Authorization: Bearer user-token" $(minikube service flask-service --url)/api/users

```

POST /api/users
To test the POST /api/users endpoint, run:
```shell
curl -X POST -H "Authorization: Bearer admin-token" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com"}' $(minikube service flask-service --url)/api/users
```

##Testing with Pytest
To run the unit tests using Pytest, execute the following command:
```shell
python -m unittest discover tests
```

## Cleaning Up
To clean up the Kubernetes resources and stop Minikube, run:
```shell
minikube stop
```