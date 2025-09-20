 Assessment-1 Containerisation and deployment of wisecow application on kubernetes with TLS certificate

 Wisecow

Wisecow is a simple web application that serves "wisdom" using **cowsay** and **fortune** in a fun way. The app is fully containerized with **Docker**, deployed on **Kubernetes**, and supports **HTTPS/TLS** with automated **CI/CD** using GitHub Actions.



Table of Contents

1. [Project Overview](#project-overview)  
2. [Prerequisites](#prerequisites)  
3. [Setup & Run Locally](#setup--run-locally)  
4. [Dockerization](#dockerization)  
5. [Kubernetes Deployment](#kubernetes-deployment)  
6. [TLS / HTTPS](#tls--https)  
7. [CI/CD Pipeline](#cicd-pipeline)  
8. [Accessing the Application](#accessing-the-application)  
9. [Contributors](#contributors)  


Project Overview

Wisecow is a lightweight fun app that:

- Serves a random “fortune” message using the `fortune` command.  
- Displays the message in a cow ASCII art using `cowsay`.  
- Runs inside a Docker container.  
- Can be deployed to Kubernetes with automatic scaling.  
- Supports secure HTTPS using TLS.


Prerequisites

Before running Wisecow locally or on Kubernetes, make sure you have:

- Ubuntu / Linux system  
- Docker installed  
- Minikube installed (for local Kubernetes cluster)  
- `kubectl` command-line tool  
- OpenSSL (for TLS certificates)  

Optional for CI/CD:

- GitHub account for GitHub Actions 
- Docker Hub account  


 Setup & Run Locally
