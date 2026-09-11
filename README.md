# Python K8s Task API

A simple Python Flask REST API containerized using Docker and deployed using Kubernetes.

## 🚀 Project Overview

This project demonstrates how to:

- Build a REST API using Python Flask
- Containerize the application using Docker
- Deploy the Docker application using Kubernetes
- Run multiple replicas using Kubernetes Deployment
- Expose the application using a Kubernetes NodePort Service
- Perform API health checks
- Manage the project using Git and GitHub

## 🛠 Technologies Used

- Python
- Flask
- Docker
- Kubernetes
- Docker Desktop
- WSL 2
- Git
- GitHub

## 🏗 Architecture

```text
             User / Browser
                    |
                    v
             Flask REST API
                    |
                    v
              Docker Image
                    |
                    v
          Kubernetes Deployment
                    |
          +---------+---------+
          |                   |
          v                   v
        Pod 1               Pod 2
          |                   |
          +---------+---------+
                    |
                    v
          Kubernetes Service
               NodePort
                    |
                    v
             User / Browser