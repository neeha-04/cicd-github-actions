# 🚀 CI/CD Pipeline for Dockerized Flask Application

A Flask-based web application integrated with a complete CI/CD pipeline using GitHub Actions, Docker, GitHub Container Registry, automated testing, security scanning, and deployment automation.

This project demonstrates modern DevOps practices including Continuous Integration, Continuous Deployment, containerization, automated testing, vulnerability scanning, and cloud-ready application delivery.

---

# 📋 Internship Details

| Field                 | Details                        |
| --------------------- | ------------------------------ |
| **Candidate Name**    | Neeharika Shakthivelan         |
| **Intern ID**         | CITS4308                       |
| **Organization**      | CodTech IT Solutions Pvt. Ltd. |
| **Domain**            | DevOps                         |
| **Project Title**     | CI/CD Pipeline for Flask Application |

---

# 🌐 Live Deployment

### Live Demo

(Add your deployment URL here)

### Available Endpoints

* Home Page: `/`
* Health Check: `/health`
* Application Information: `/api/info`
* Addition API: `/api/add`
* Subtraction API: `/api/subtract`
* Pipeline Status: `/api/pipeline-status`

---

# 📖 Project Overview

This project demonstrates the implementation of a complete CI/CD workflow for a Flask web application.

The application is containerized using Docker and automatically built, tested, scanned, and deployed through GitHub Actions.

The pipeline ensures that every code change goes through automated validation before deployment, following real-world DevOps practices.

---

# 🎯 Objectives

* Build a production-ready Flask application.
* Containerize the application using Docker.
* Automate testing and deployment using GitHub Actions.
* Perform security scanning using Trivy.
* Publish Docker images using GitHub Container Registry.
* Implement Continuous Integration and Continuous Deployment workflow.
* Understand modern DevOps automation practices.

---

# 🚀 Features

✅ Flask REST Web Application

✅ Docker Containerization

✅ GitHub Actions CI/CD Pipeline

✅ Automated Testing

✅ Python Version Matrix Testing

✅ Docker Image Build Automation

✅ Docker Image Publishing

✅ GitHub Container Registry Integration

✅ Trivy Security Vulnerability Scanning

✅ Deployment Automation

✅ API Health Monitoring

✅ Pipeline Status Endpoint

---

# 🏗️ CI/CD Architecture

```text
Developer Push
       │
       ▼
GitHub Repository
       │
       ▼
GitHub Actions Workflow
       │
       ├── Code Linting
       │
       ├── Automated Tests
       │
       ├── Docker Build
       │
       ├── Smoke Testing
       │
       ├── Security Scan (Trivy)
       │
       ├── Push Docker Image
       │
       ▼
Deployment Environment
```

---

# 🔄 CI/CD Pipeline Stages

| Stage | Description |
|------|-------------|
| Lint | Checks code quality |
| Test | Runs automated tests |
| Docker Build | Creates application container |
| Smoke Test | Validates container execution |
| Security Scan | Detects vulnerabilities |
| Push Image | Uploads image to GHCR |
| Deploy | Releases application |

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Backend Development |
| Flask | Web Framework |
| Docker | Containerization |
| GitHub Actions | CI/CD Automation |
| GitHub Container Registry | Docker Image Storage |
| Gunicorn | Production WSGI Server |
| Pytest | Automated Testing |
| Flake8 | Code Quality Checking |
| Trivy | Security Scanning |
| HTML/CSS | Frontend Interface |

---

# 📁 Project Structure

```text
cicd-github-actions/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── templates/
│
├── tests/
│   └── test_app.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
├── requirements.txt
├── requirements-dev.txt
├── run.py
├── .dockerignore
├── README.md
└── docker-compose.yml
```

---

# ⚙️ Installation and Setup

## Clone Repository

```bash
git clone https://github.com/neeha-04/cicd-github-actions.git

cd cicd-github-actions
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

For development:

```bash
pip install -r requirements-dev.txt
```

---

# ▶️ Run Application Locally

```bash
python run.py
```

Application runs on:

```text
http://localhost:5000
```

---

# 🐳 Docker Setup

## Build Docker Image

```bash
docker build -t flask-cicd-app .
```

---

## Run Container

```bash
docker run -p 5000:5000 flask-cicd-app
```

---

## View Running Containers

```bash
docker ps
```

---

## Stop Container

```bash
docker stop <container_id>
```

---

# 🌐 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Home Page |
| `/health` | Health Check |
| `/api/info` | Application Information |
| `/api/add` | Addition API |
| `/api/subtract` | Subtraction API |
| `/api/pipeline-status` | CI/CD Pipeline Information |

---

# 🧪 Testing

Run automated tests:

```bash
pytest
```

Run code quality checks:

```bash
flake8 .
```

---

# 🔐 Security Features

* Docker container isolation
* Automated vulnerability scanning using Trivy
* Secure GitHub Actions workflow
* Environment variable support
* Production server using Gunicorn
* Automated validation before deployment

---

# 📦 Docker Image Workflow

```text
Code Commit
     │
     ▼
GitHub Actions
     │
     ▼
Docker Build
     │
     ▼
Security Scan
     │
     ▼
GitHub Container Registry
     │
     ▼
Deployment
```

---

# 📚 Learning Outcomes

Through this project, the following skills were developed:

* CI/CD Pipeline Development
* GitHub Actions Automation
* Docker Container Management
* Automated Testing
* Security Scanning
* Container Registry Usage
* Deployment Automation
* DevOps Workflow Implementation
* Production Application Deployment

---

# ✅ Conclusion

The CI/CD Pipeline for Flask Application project successfully demonstrates the automation of software delivery using modern DevOps tools.

The project integrates Flask, Docker, GitHub Actions, automated testing, security scanning, and container publishing to create a reliable and production-ready deployment workflow.

This project provided practical experience in implementing real-world DevOps automation and continuous delivery practices.

---

# 🔗 Project Links

### GitHub Repository

https://github.com/neeha-04/cicd-github-actions

### Docker Image

(Add GHCR Image Link)

### Live Deployment

(Add Deployment Link)

---

# 👩‍💻 Author

**Neeharika Shakthivelan**

DevOps Intern  
CodTech IT Solutions Pvt. Ltd.

**Intern ID:** CITS4308

---

## ⭐ Acknowledgement

This project was developed as part of the DevOps Internship Program offered by CodTech IT Solutions Pvt. Ltd.

The internship provided practical exposure to CI/CD pipelines, Docker, GitHub Actions, automated testing, security practices, container management, and modern DevOps workflows.