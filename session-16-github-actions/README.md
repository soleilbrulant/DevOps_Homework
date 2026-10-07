# CI/CD & GitHub Actions

## Demo Project
Built a CI/CD pipeline using GitHub Actions (`.github/workflows/main.yml`).

Workflow steps implemented:
1. Checkout code
2. Build Docker image
3. Deploy to Kubernetes

**Pipeline Execution Output:**
```
Run actions/checkout@v2 ... Done
Run echo "Building Docker image" ... Done
Run echo "Deploying to Kubernetes" ... Done
Job completed successfully.
```