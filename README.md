# Web-App API – Cloud Native DevOps Deployment

A full-stack Web-App API project demonstrating modern DevOps practices, including CI/CD automation, containerization, Kubernetes orchestration, and Infrastructure as Code (IaC) using Terraform.

## 🚀 Project Overview

Web-App API is a full-stack Todo application consisting of separate frontend, backend, and database components.

The project focuses on automating application deployment, managing infrastructure, and orchestrating containerized workloads using Azure DevOps, Kubernetes, and Terraform.

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| CI/CD | Azure DevOps |
| Infrastructure as Code | Terraform |
| Containerization | Docker, Docker Compose |
| Container Orchestration | Kubernetes |
| Database | PostgreSQL |
| Version Control | Git, GitHub |
| Application Architecture | Frontend, Backend, Database |

## 🏗️ Application Architecture

The application consists of three primary components:

- **Frontend:** User interface for managing Todo tasks.
- **Backend:** Handles application logic and API requests.
- **Database:** PostgreSQL for persistent data storage.

## 🔄 Deployment Workflow

1. Push application code to the Git repository.
2. Azure DevOps triggers the CI/CD pipeline.
3. Build and validate application components.
4. Build Docker images for frontend and backend.
5. Provision infrastructure using Terraform.
6. Deploy containerized workloads to Kubernetes.
7. Validate application deployment and service availability.

## 📁 Repository Structure

```text
web-app-api/
│
├── backend/
│   └── Backend application source
│
├── frontend/
│   └── Frontend application source
│
├── .github/
│   └── workflows/
│
├── .env.example
├── .gitignore
├── docker-compose.yml
└── README.md
```

## ⚙️ Local Setup

### Prerequisites

- Git
- Docker
- Docker Compose

### 1. Clone the repository

```bash
git clone https://github.com/reddynaveen0106/webapp-api.git
cd webapp-api
```

### 2. Configure environment variables

```bash
cp .env.example .env
```

Configure the required database credentials and application settings in `.env`.

### 3. Build and run the application

```bash
docker compose up -d --build
```

### 4. Verify running containers

```bash
docker compose ps
```

### 5. Stop the application

```bash
docker compose down
```

## ☸️ Kubernetes Deployment

Kubernetes is used to orchestrate containerized application workloads.

Key deployment considerations:

- Deploy frontend and backend as separate workloads.
- Configure Kubernetes Deployments and Services.
- Manage application configurations using ConfigMaps and Secrets.
- Configure health checks and resource requests/limits.
- Use rolling updates for application releases.

## 🏗️ Infrastructure as Code – Terraform

Terraform is used to define and provision the required infrastructure.

Key practices:

- Declarative infrastructure provisioning.
- Repeatable infrastructure deployments.
- Terraform state management.
- Infrastructure planning and validation.
- Consistent infrastructure configuration.

## 🔄 CI/CD – Azure DevOps

Azure DevOps is used to automate the application delivery process.

Pipeline activities include:

- Source code integration.
- Build and validation stages.
- Docker image creation and publishing.
- Infrastructure provisioning and updates.
- Kubernetes application deployment.
- Deployment validation.

## 🎯 Project Objectives

- Implement automated CI/CD workflows.
- Containerize frontend and backend services.
- Deploy applications using Kubernetes.
- Provision infrastructure using Terraform.
- Improve deployment consistency and reliability.
- Apply practical DevOps and cloud-native engineering practices.

## 👨‍💻 Author

**Naveen Reddy**

DevOps | Cloud | Kubernetes | Infrastructure Automation

GitHub: [reddynaveen0106](https://github.com/reddynaveen0106)

---

*Web-App API demonstrates practical DevOps implementation for deploying and managing a containerized full-stack application.*
