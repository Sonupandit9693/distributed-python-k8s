# Distributed Python Microservices with Kubernetes

A **microservices-based** system built using **Python** and deployed on **Kubernetes**. It includes authentication, API gateway, interservice communication, and RabbitMQ for event-driven processing.

## 📌 Features
- **Auth Service** – JWT-based authentication  
- **API Gateway** – Handles requests & routes to services  
- **RabbitMQ** – Asynchronous messaging  
- **MongoDB & GridFS** – File storage  
- **Interservice Communication** – Sync (HTTP) & Async (Events)  
- **Kubernetes Deployments** – StatefulSet, Ingress  

## 🚀 Setup & Installation
```sh
git clone https://github.com/Sonupandit9693/distributed-python-k8s.git
cd distributed-python-k8s
```

### 🔹 Start Services with Docker
```sh
docker-compose up --build
```

### 🔹 Deploy to Kubernetes
```sh
kubectl apply -f k8s/
```

## 🏗️ Architecture Overview
- **Auth Service:** Handles user authentication (JWT).  
- **Gateway Service:** Routes requests to internal services.  
- **Converter Service:** Processes data conversions.  
- **Notification Service:** Sends email/SMS notifications.  

## 🛠 Technologies Used
- **Python (FastAPI)**  
- **Docker & Kubernetes**  
- **RabbitMQ**  
- **MongoDB & GridFS**  
- **gRPC & REST API**  

## 📬 Contributing
Feel free to fork this repository and submit PRs! 🚀

## 📄 License
MIT License

