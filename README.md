 Assessment-1 Containerisation and deployment of wisecow application on kubernetes with TLS certificate1. Introduction

Wisecow is a fun and lightweight application that generates random wisdom messages using fortune and displays them in a cow ASCII art with cowsay. The primary goal of this project is to demonstrate the end-to-end DevOps workflow, including containerization, Kubernetes deployment, secure communication with TLS, and automated CI/CD pipelines.

2. Objective

The main objectives of the project were:

Containerize the Wisecow application using Docker.

Deploy it to a Kubernetes environment for orchestration and scalability.

Enable secure communication through TLS/HTTPS.

Implement continuous integration and deployment using GitHub Actions.

3. Steps Involved
3.1 Containerization

The Wisecow application was packaged into a Docker container. This ensured that the application and its dependencies (cowsay and fortune) could run consistently across different environments. Containerization makes the application portable, scalable, and easy to deploy.

3.2 Kubernetes Deployment

The containerized application was deployed to a Kubernetes cluster. This included:

Defining a Deployment to manage application replicas.

Creating a Service to expose the application within the cluster and externally.

Ensuring that pods start successfully and remain healthy.

Kubernetes provided orchestration, scaling, and self-healing capabilities for the application.

3.3 TLS / HTTPS Configuration

To secure the application, TLS certificates were implemented. This involved:

Generating a self-signed certificate and key.

Creating a Kubernetes TLS secret to store the certificate.

Configuring an Ingress resource to serve the application over HTTPS.

This step ensured that all communication with the Wisecow application was encrypted, fulfilling security best practices.

3.4 CI/CD Pipeline with GitHub Actions

A GitHub Actions workflow was implemented to automate:

Building the Docker image whenever code changes are pushed.

Pushing the image to Docker Hub for easy distribution.

Updating the Kubernetes deployment automatically with the new image.

This automated pipeline ensured that the application could be continuously deployed with minimal manual intervention, demonstrating modern DevOps practices.

4. Results

Wisecow runs successfully in a Kubernetes cluster with multiple replicas.

TLS/HTTPS is implemented, securing the communication.

CI/CD pipeline ensures automatic updates and deployments on code changes.

The project demonstrates a complete DevOps workflow from development to deployment.

5. Conclusion

The Wisecow project showcases the integration of containerization, orchestration, security, and automation. It highlights essential DevOps skills such as:

Docker containerization

Kubernetes deployment and service management

TLS/HTTPS configuration

Continuous integration and deployment with GitHub Actions

This Assessment demonstrates the ability to deliver cloud-native applications with secure, automated, and scalable deployments.

Done by: Mohamed Askhaf, B.Tech IT
