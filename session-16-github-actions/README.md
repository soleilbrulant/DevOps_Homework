# CI/CD & GitHub Actions

## Demo Project
This project sets up a CI/CD pipeline using GitHub Actions.

- **CI (Continuous Integration)**: Automates building and testing code on every push.
- **CD (Continuous Deployment)**: Automates deployment to the server/cluster.

Workflow steps implemented:
1. Checkout code
2. Setup Node.js
3. Install dependencies and run tests
4. Build Docker image
5. Push to Docker Hub
6. Deploy to Kubernetes

All steps ran successfully. Check the `.github/workflows/main.yml` for the pipeline definition.
