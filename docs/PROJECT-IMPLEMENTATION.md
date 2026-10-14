# E-Commerce DevOps Project Implementation

## 1. Project Overview
This project demonstrates a DevOps and cloud-native delivery workflow for a Flask-based e-commerce application.

## 2. Application
- Flask application with health and product endpoints.
- Custom Prometheus metrics endpoint: /metrics.
- Automated application tests using pytest.

## 3. CI/CD and Containerization
- GitHub for source code management.
- Jenkins for automated checkout, build, testing, Docker build and security scanning.
- Docker and Docker Compose for containerization.

## 4. Infrastructure and Deployment
- Terraform for Docker infrastructure provisioning.
- Ansible for automation.
- Kubernetes for application deployment.
- Helm for Kubernetes package management.

## 5. Monitoring and Alerting
- Prometheus collects application metrics.
- Grafana visualizes application health.
- Grafana alert rule monitors ecommerce_app_up and triggers when its value falls below 1.

## 6. Logging
- Kubernetes application logs are collected using kubectl.
- A Bash script at scripts/analyze-logs.sh summarizes log lines, successful HTTP requests and client/server errors.
- Centralized ELK logging is not yet verified.

## 7. Security
- Trivy is used for container image security scanning.
- Scan reports are stored in the reports directory.
- Review and remediate detected vulnerabilities before production use.

## 8. Limitations and Future Work
- Configure and test centralized logging.
- Complete AI-assisted incident analysis.
- Validate cloud deployment in AWS.
- Review alert delivery and security findings.

## 9. Repository
https://github.com/HarshitMali930/final-ecommerce-devops
