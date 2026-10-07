# DevSecOps Demo Project

This project integrates security into the CI/CD pipeline.

## Flow
Code -> Build -> Unit Test -> SAST (SonarQube/Trivy) -> SCA (Trivy) -> Secret Scan (TruffleHog/Trivy) -> Docker Build -> Container Image Scan -> Security Gate -> Push Image -> Deploy to K8s.

## Implementation
Configured GitHub Actions to run Trivy for vulnerability scanning on the Docker image before pushing. Secret scanning is done using the default GitHub Advanced Security features.
