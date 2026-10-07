# Final DevOps Project

## Overview
This is the final capstone project covering the entire DevOps lifecycle.

## Pipeline Flow
1. Code pushed to GitHub.
2. GitHub Actions triggers CI.
3. Runs unit tests and Trivy security scans.
4. Builds Docker image and pushes to container registry.
5. Updates Helm chart values in the GitOps repository.
6. ArgoCD (GitOps) syncs the new Helm chart to the Kubernetes cluster.
7. Application runs with HPA, Probes, and Persistent Storage.

## Infrastructure
Terraform was used to provision the EKS cluster and VPC.

## Troubleshooting Challenge
Introduced a faulty image tag and a bad readiness probe. Detected the issue via ArgoCD sync failure and `kubectl describe pod`. Fixed the helm chart and pushed, allowing GitOps to reconcile and fix the deployment automatically.
