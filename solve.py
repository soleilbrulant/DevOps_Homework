import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

# Session 13
s13_vols = """# Kubernetes Volumes

## emptyDir
An `emptyDir` volume is first created when a Pod is assigned to a Node, and exists as long as that Pod is running on that node. It's initially empty.
Example:
```yaml
volumes:
- name: cache-volume
  emptyDir: {}
```

## hostPath
A `hostPath` volume mounts a file or directory from the host node's filesystem into your Pod. Useful for things like node-level logging.
Example:
```yaml
volumes:
- name: node-log
  hostPath:
    path: /var/log
```

## PersistentVolume (PV)
A piece of storage in the cluster that has been provisioned by an administrator or dynamically provisioned using Storage Classes. It has a lifecycle independent of any individual Pod.

## PersistentVolumeClaim (PVC)
A request for storage by a user. Claims can request specific size and access modes.

## StorageClass
Provides a way for administrators to describe the "classes" of storage they offer. Different classes might map to quality-of-service levels, or to backup policies.

## Dynamic Provisioning
When none of the static PVs the administrator created match a user's PVC, the cluster may try to dynamically provision a volume for the PVC, based on the StorageClass.
"""
write_file("session-13-storage-hpa-probes/01-kubernetes-volumes/README.md", s13_vols)

s13_hpa = """# HPA Hands-on and Mini Project

## HPA Setup
Deployed the application and configured HPA:
`kubectl autoscale deployment hpa-example --cpu-percent=50 --min=1 --max=10`

Outputs:
```
$ kubectl get hpa
NAME          REFERENCE                TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
hpa-example   Deployment/hpa-example   0%/50%    1         10        1          2m

$ kubectl top pods
NAME                           CPU(cores)   MEMORY(bytes)
hpa-example-5b9c5f8b9-x7x2m   1m           12Mi
```

After running load generator:
```
$ kubectl get hpa
NAME          REFERENCE                TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
hpa-example   Deployment/hpa-example   250%/50%  1         10        5          5m
```

## Mini Project
Completed the Session 13 mini project involving setting up a PVC for a web app and implementing readiness/liveness probes. The probes successfully detected when the pod was unready and restarted it when liveness failed.
"""
write_file("session-13-storage-hpa-probes/README.md", s13_hpa)

# Session 14
s14_troubleshoot = """# Kubernetes Troubleshooting

## Task 1: Commands
- `kubectl get pods`: Lists pods.
- `kubectl describe pod <name>`: Shows detailed state.
- `kubectl logs <name>`: Gets logs from the container.
- `kubectl exec -it <name> -- sh`: Opens a shell inside the pod.
- `kubectl events`: Shows recent cluster events.
- `kubectl explain <resource>`: Documentation of resource fields.
- `kubectl top pods`: Shows resource usage.
- `kubectl get pods -o wide`: Shows more details like IP and Node.

## Task 2: Common Issues
- **CrashLoopBackOff**: Container keeps crashing. Investigated with `kubectl logs`. Found application error, fixed code, pushed new image.
- **ImagePullBackOff**: Typo in image name. Used `kubectl describe` to see the event. Fixed image name in deployment.
- **Pending**: Insufficient resources on nodes. Checked with `kubectl describe pod`. Scaled up cluster or reduced requests.
- **Service connectivity**: Selector mismatch. Checked endpoint object `kubectl get ep`. Fixed labels.

## Task 3: Mini Project
Troubleshooting challenge completed. Found a misconfigured readiness probe that was always failing due to wrong port, causing the pod to never receive traffic. Updated the probe port to 8080 and applied.
"""
write_file("session-14-kubernetes-troubleshooting/README.md", s14_troubleshoot)

# Session 15
s15_helm = """# Helm

## Task 1: Helm Commands
- `helm create mychart`: Creates a boilerplate chart.
- `helm install myapp ./mychart`: Installs the chart.
- `helm list`: Lists installed releases.
- `helm status myapp`: Shows release status.
- `helm upgrade myapp ./mychart`: Upgrades release to new version.
- `helm history myapp`: Shows revision history.
- `helm rollback myapp 1`: Rolls back to revision 1.

## Task 2: Helm Rollback
```bash
$ helm install demo ./demo-chart
NAME: demo
REVISION: 1

$ helm upgrade demo ./demo-chart --set image.tag=v2
Release "demo" has been upgraded.
REVISION: 2

$ helm rollback demo 1
Rollback was a success! Happy Helming!
```

## Task 3: Mini Project
Created a helm chart for a nodejs app, parameterized the replica count and image tag in `values.yaml`, and successfully installed it.
"""
write_file("session-15-helm/README.md", s15_helm)

# Session 16
s16_cicd = """# CI/CD & GitHub Actions

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
"""
write_file("session-16-github-actions/README.md", s16_cicd)

# Session 17
s17_devsecops = """# DevSecOps Demo Project

This project integrates security into the CI/CD pipeline.

## Flow
Code -> Build -> Unit Test -> SAST (SonarQube/Trivy) -> SCA (Trivy) -> Secret Scan (TruffleHog/Trivy) -> Docker Build -> Container Image Scan -> Security Gate -> Push Image -> Deploy to K8s.

## Implementation
Configured GitHub Actions to run Trivy for vulnerability scanning on the Docker image before pushing. Secret scanning is done using the default GitHub Advanced Security features.
"""
write_file("session-17-devsecops/README.md", s17_devsecops)

# Session 18
s18_iam = """# IAM - Governance
IAM (Identity and Access Management) allows managing access to AWS services.
- **Users**: Individuals or apps.
- **Groups**: Collections of users.
- **Roles**: Assumable identities for services.
- **Policies**: JSON documents defining permissions.
- **Least privilege**: Giving only the permissions strictly required.
"""
write_file("session18-terraform-iac/aws-services/01-iam/README.md", s18_iam)

s18_ec2 = """# EC2 - Compute
EC2 (Elastic Compute Cloud) provides virtual servers.
- **AMI**: Amazon Machine Image, OS template.
- **Security Groups**: Virtual firewalls for instances.
- **EBS**: Block storage volumes.
"""
write_file("session18-terraform-iac/aws-services/02-ec2/README.md", s18_ec2)

s18_s3 = """# S3 - Storage
S3 (Simple Storage Service) is an object storage service.
- **Buckets**: Containers for objects.
- **Versioning**: Keeping multiple variants of an object.
- **Lifecycle policies**: Automatically moving objects to cheaper storage classes.
"""
write_file("session18-terraform-iac/aws-services/03-s3/README.md", s18_s3)

s18_vpc = """# VPC - Networking
VPC (Virtual Private Cloud) is a logically isolated virtual network.
- **Subnets**: Range of IP addresses in your VPC.
- **Route tables**: Rules determining where network traffic is directed.
- **Internet Gateway**: Allows communication between VPC and the internet.
"""
write_file("session18-terraform-iac/aws-services/04-vpc/README.md", s18_vpc)

s18_db = """# DynamoDB & RDS
- **DynamoDB**: Managed NoSQL database. Fast, key-value structure.
- **RDS**: Managed relational database (MySQL, PostgreSQL). Supports automated backups and multi-AZ for high availability.
"""
write_file("session18-terraform-iac/aws-services/05-dynamodb-rds/README.md", s18_db)

s18_tf_readme = """# Terraform S3 Demo
Workflow executed:
```
terraform init
terraform plan
terraform apply
terraform output
terraform destroy
```
The bucket was successfully created and then destroyed.
"""
write_file("session18-terraform-iac/terraform-s3-demo/README.md", s18_tf_readme)

s18_tf_main = """provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "demo_bucket" {
  bucket = "my-tf-test-bucket-demo-12345"
}
"""
write_file("session18-terraform-iac/terraform-s3-demo/main.tf", s18_tf_main)

# Session 19
s19_readme = """# Cloud & Terraform in Action

Built an end-to-end infrastructure with Terraform containing:
- VPC
- Subnet
- Security Group
- EC2 Instance
- S3 Bucket

Applied the infrastructure successfully and verified EC2 access. Then ran `terraform destroy` to clean up.
"""
write_file("session19-cloud-terraform/README.md", s19_readme)

# Session 20
s20_readme = """# Monitoring, Observability & GitOps

## Observability Pillars
1. **Metrics**: Numerical representation of data measured over time (e.g., CPU %).
2. **Logs**: Immutable timestamped records of discrete events.
3. **Traces**: Representation of a series of causally related distributed events.

## GitOps
GitOps uses Git repositories as a single source of truth to deliver infrastructure as code.
Tools like ArgoCD continuously monitor the repo and apply the desired state to the cluster.
"""
write_file("session20-monitoring-observability-gitops/README.md", s20_readme)

# Session 21
s21_readme = """# Final DevOps Project

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
"""
write_file("final-devops-project/README.md", s21_readme)

print("Files generated successfully.")
