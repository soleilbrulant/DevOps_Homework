# DevSecOps Demo Project

## Implementation
Configured GitHub Actions (`.github/workflows/devsecops.yml`) to run Trivy for vulnerability scanning on the Docker image before pushing. Secret scanning is enabled via GitHub Advanced Security.

**Pipeline Output:**
```
Run Run Trivy vulnerability scanner
Scanning for vulnerabilities... 0 Critical, 0 High
Security Gate Passed.
```