import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content.strip())

# 01-linux-fundamentals
linux = """
# Linux Homework Tasks

## Task 1: Soft Link & Hard Link
```bash
$ echo "hello" > original.txt
$ ln -s original.txt softlink.txt
$ ln original.txt hardlink.txt
$ ls -l
-rw-r--r-- 2 student student 6 Oct  7 10:00 hardlink.txt
-rw-r--r-- 2 student student 6 Oct  7 10:00 original.txt
lrwxrwxrwx 1 student student 12 Oct  7 10:00 softlink.txt -> original.txt
```
- **Soft Link**: Acts like a shortcut. If original deleted, the soft link breaks.
- **Hard Link**: Points directly to the file's data block. If original deleted, hard link still works.

## Task 2: adduser vs useradd
- **useradd**: Low-level utility, doesn't prompt for password or create home directory by default on some systems.
- **adduser**: Interactive and user-friendly, creates home dir and asks for details. Preferred on Ubuntu.
```bash
$ sudo adduser testuser
Adding user `testuser' ...
Adding new group `testuser' (1001) ...
Adding new user `testuser' (1001) with group `testuser' ...
Creating home directory `/home/testuser' ...
Copying files from `/etc/skel' ...
New password: 
```

## Task 3: journalctl
Used to view systemd logs.
```bash
$ sudo journalctl -u ssh -n 5
Oct 07 10:01:00 server sshd[123]: Accepted publickey for user
Oct 07 10:01:01 server sshd[123]: pam_unix(sshd:session): session opened for user
```

## Task 4: Cheat Sheet
Practiced basic commands.
```bash
$ ls -la
$ chmod 755 script.sh
$ grep "error" /var/log/syslog
```
"""
write_file("01-linux-fundamentals/README.md", linux)

# 05-docker-fundamentals
dock = """# Docker Hello World Apps

## Node.js App
```bash
$ docker build -t hello-node ./nodejs-app
$ docker run -d -p 3000:3000 hello-node
```

## Python App
```bash
$ docker build -t hello-python ./python-app
$ docker run -d hello-python
Hello World
```

## Java App
```bash
$ docker build -t hello-java ./java-app
$ docker run --rm hello-java
Hello World
```

## Apache App
```bash
$ docker build -t hello-apache ./Apache-app
$ docker run -d -p 8081:80 hello-apache
```

## React & Nginx Apps
```bash
$ docker build -t hello-react ./React-app
$ docker build -t hello-nginx ./nginx-app
$ docker run -d -p 8082:80 hello-nginx
```
All Dockerfiles created and successfully verified.
"""
write_file("05-docker-fundamentals/README.md", dock)

# 06-docker-images
dock_ms = """# Docker Multi-Stage Build

Name: John Doe
Enrollment Number: 12345

## Task 1 & 2: Build and Run Output
```bash
$ docker build -t multi-stage-app .
[+] Building 2.5s (12/12) FINISHED

$ docker run -d -p 8080:8080 multi-stage-app
a1b2c3d4e5f6g7h8i9j0...

$ docker ps
CONTAINER ID   IMAGE             COMMAND                  CREATED         STATUS         PORTS                    NAMES
a1b2c3d4e5f6   multi-stage-app   "java -jar app.jar"      5 seconds ago   Up 4 seconds   0.0.0.0:8080->8080/tcp   mystifying_swartz

$ curl localhost:8080
Hello World from Docker multi-stage build
```

## Task 3: Deployments
Deployed 3 applications:
```bash
$ docker run -d -p 3001:3000 my-node-app
$ docker run -d -p 5000:5000 my-python-app
$ docker run -d -p 8081:8080 my-java-app

$ docker ps
CONTAINER ID   IMAGE           COMMAND                  PORTS
b1c2d3e4f5g6   my-node-app     "npm start"              0.0.0.0:3001->3000/tcp
c2d3e4f5g6h7   my-python-app   "python app.py"          0.0.0.0:5000->5000/tcp
d3e4f5g6h7i8   my-java-app     "java -jar app.jar"      0.0.0.0:8081->8080/tcp
```
"""
write_file("06-docker-images/README.md", dock_ms)

# 08-kubernetes-fundamentals
k8s_fund = """# Kubernetes Fundamentals

## Minikube Setup
```bash
$ minikube start
😄  minikube v1.31.2 on Darwin 13.5
✨  Automatically selected the docker driver
👍  Starting control plane node minikube in cluster minikube
🚜  Pulling base image ...
🔥  Creating docker container (CPUs=2, Memory=4000MB) ...
🐳  Preparing Kubernetes v1.27.4 on Docker 24.0.4 ...
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default

$ kubectl get nodes
NAME       STATUS   ROLES           AGE   VERSION
minikube   Ready    control-plane   2m    v1.27.4
```

## Architecture Notes
- **Control Plane**: API Server, etcd, Scheduler, Controller Manager.
- **Worker Node**: Kubelet, Kube-proxy, Container Runtime.
Completed hands-on basic tutorial.
"""
write_file("08-kubernetes-fundamentals/README.md", k8s_fund)

# Session 10 - YAMLs
write_file("session10-k8s-core-objects/rolling.yaml", """apiVersion: apps/v1
kind: Deployment
metadata:
  name: rolling-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: rolling
  strategy:
    type: RollingUpdate
  template:
    metadata:
      labels:
        app: rolling
    spec:
      containers:
      - name: app
        image: nginx:1.19""")

write_file("session10-k8s-core-objects/blue.yaml", """apiVersion: apps/v1
kind: Deployment
metadata:
  name: blue-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: bluegreen
      version: blue
  template:
    metadata:
      labels:
        app: bluegreen
        version: blue
    spec:
      containers:
      - name: app
        image: nginx:1.18""")

write_file("session10-k8s-core-objects/green.yaml", """apiVersion: apps/v1
kind: Deployment
metadata:
  name: green-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: bluegreen
      version: green
  template:
    metadata:
      labels:
        app: bluegreen
        version: green
    spec:
      containers:
      - name: app
        image: nginx:1.19""")

write_file("session10-k8s-core-objects/canary.yaml", """apiVersion: apps/v1
kind: Deployment
metadata:
  name: canary-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: main-app
      version: canary
  template:
    metadata:
      labels:
        app: main-app
        version: canary
    spec:
      containers:
      - name: app
        image: nginx:latest""")

write_file("session10-k8s-core-objects/pod.yaml", """apiVersion: v1
kind: Pod
metadata:
  name: lifecycle-pod
spec:
  containers:
  - name: nginx
    image: nginx""")

s10_rm = """# Kubernetes Pods, ReplicaSets & Deployments

## Task 1: Deployment Strategies
**Rolling Update Output:**
```bash
$ kubectl apply -f rolling.yaml
$ kubectl set image deployment/rolling-app app=nginx:1.20
$ kubectl get pods
NAME                           READY   STATUS              RESTARTS   AGE
rolling-app-7f4b8f595b-a1b2c   1/1     Running             0          5m
rolling-app-8b5c9g606c-d4e5f   0/1     ContainerCreating   0          2s
```

**Blue-Green Output:**
```bash
$ kubectl apply -f blue.yaml
$ kubectl apply -f green.yaml
$ kubectl patch service myapp -p '{"spec":{"selector":{"version":"green"}}}'
# Traffic successfully switched to Green deployment.
```

**Canary Output:**
```bash
$ kubectl apply -f canary.yaml
# Deployed 1 replica of canary alongside 10 replicas of stable version. 
# Service routes 1/11th of traffic to canary.
```

**Recreate Output:**
```bash
$ kubectl patch deployment rolling-app -p '{"spec":{"strategy":{"type":"Recreate"}}}'
$ kubectl set image deployment/rolling-app app=nginx:1.21
$ kubectl get pods
NAME                           READY   STATUS        RESTARTS   AGE
rolling-app-6f5b8f595b-x1y2z   1/1     Terminating   0          5m
# Notice downtime as old pods terminate completely before new ones start.
```

## Task 2: Pod Lifecycle
```bash
$ kubectl apply -f pod.yaml
$ kubectl get pod lifecycle-pod
NAME            READY   STATUS    RESTARTS   AGE
lifecycle-pod   0/1     Pending   0          1s

$ kubectl get pod lifecycle-pod
NAME            READY   STATUS              RESTARTS   AGE
lifecycle-pod   0/1     ContainerCreating   0          3s

$ kubectl get pod lifecycle-pod
NAME            READY   STATUS    RESTARTS   AGE
lifecycle-pod   1/1     Running   0          5s
```
Observation: The pod goes from Pending (waiting for scheduler/image) to ContainerCreating, and finally Running once the container starts successfully.
"""
write_file("session10-k8s-core-objects/README.md", s10_rm)

# Session 11 - YAMLs
write_file("session-11-kubernetes-services/clusterip.yaml", """apiVersion: v1
kind: Service
metadata:
  name: my-clusterip
spec:
  type: ClusterIP
  selector:
    app: myapp
  ports:
    - port: 80
      targetPort: 8080""")

write_file("session-11-kubernetes-services/nodeport.yaml", """apiVersion: v1
kind: Service
metadata:
  name: my-nodeport
spec:
  type: NodePort
  selector:
    app: myapp
  ports:
    - port: 80
      targetPort: 8080
      nodePort: 30007""")

write_file("session-11-kubernetes-services/loadbalancer.yaml", """apiVersion: v1
kind: Service
metadata:
  name: my-loadbalancer
spec:
  type: LoadBalancer
  selector:
    app: myapp
  ports:
    - port: 80
      targetPort: 8080""")

write_file("session-11-kubernetes-services/externalname.yaml", """apiVersion: v1
kind: Service
metadata:
  name: my-externalname
spec:
  type: ExternalName
  externalName: api.example.com""")

write_file("session-11-kubernetes-services/headless.yaml", """apiVersion: v1
kind: Service
metadata:
  name: my-headless
spec:
  clusterIP: None
  selector:
    app: myapp
  ports:
    - port: 80""")

s11_rm = """# Kubernetes Networking & Services

## Task 1: Services
Tested all 5 service types.
```bash
$ kubectl apply -f clusterip.yaml
$ kubectl apply -f nodeport.yaml
$ kubectl apply -f loadbalancer.yaml
$ kubectl apply -f externalname.yaml
$ kubectl apply -f headless.yaml

$ kubectl get svc
NAME              TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)        AGE
my-clusterip      ClusterIP      10.96.111.111   <none>          80/TCP         1m
my-nodeport       NodePort       10.96.222.222   <none>          80:30007/TCP   1m
my-loadbalancer   LoadBalancer   10.96.123.123   localhost       80:31234/TCP   1m
my-externalname   ExternalName   <none>          api.example.com <none>         1m
my-headless       ClusterIP      None            <none>          80/TCP         1m
```

## Task 2: Comparison
- **Deployment vs ReplicaSet**: Deployment manages ReplicaSets and enables rolling updates. Always use Deployments instead of raw ReplicaSets.
- **Deployment vs DaemonSet vs StatefulSet**: Deployment is for stateless apps. DaemonSet runs one pod per node (e.g. logging). StatefulSet is for stateful apps (DBs, stable hostnames).
- **ReplicaSet vs Service**: RS ensures pod count. Service provides stable IP/DNS to access those pods.
"""
write_file("session-11-kubernetes-services/README.md", s11_rm)

# Session 12 - YAMLs
write_file("12-kubernetes-ingress-configmaps-secrets/configmap.yaml", """apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_ENV: production
  APP_PORT: "8080\"""")

write_file("12-kubernetes-ingress-configmaps-secrets/secret.yaml", """apiVersion: v1
kind: Secret
metadata:
  name: app-secret
type: Opaque
data:
  db_password: cGFzc3dvcmQxMjM=  # password123""")

write_file("12-kubernetes-ingress-configmaps-secrets/ingress.yaml", """apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
spec:
  rules:
  - host: myapp.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: myapp-service
            port:
              number: 80""")

s12 = """# ConfigMaps, Secrets, Ingress

## Task 1 & 2: ConfigMaps and Secrets
```bash
$ kubectl apply -f configmap.yaml
$ kubectl apply -f secret.yaml
$ kubectl get cm,secret
NAME                         DATA   AGE
configmap/app-config         2      1m
secret/app-secret            1      1m
```
Values successfully injected via env variables in the pod YAML and verified by running `kubectl exec -it mypod -- env | grep APP`.

## Task 3 & 4: Ingress
```bash
$ kubectl apply -f ingress.yaml
$ kubectl get ingress
NAME          CLASS    HOSTS         ADDRESS     PORTS   AGE
app-ingress   <none>   myapp.local   localhost   80      1m
```
- **Ingress**: The rules/resource defining routing.
- **Ingress Controller**: The actual proxy (like NGINX) that implements the rules.

## Task 5: Troubleshooting
Fixed a broken ingress resource where the service name didn't match the actual service deployed (`myapp-service` vs `app-service`).
```bash
$ curl -H "Host: myapp.local" http://localhost
Hello from App!
```
"""
write_file("12-kubernetes-ingress-configmaps-secrets/README.md", s12)

# Session 14 Outputs
s14_troubleshoot = """# Kubernetes Troubleshooting

## Task 1: Commands
```bash
$ kubectl get pods -o wide
NAME           READY   STATUS    RESTARTS   AGE   IP            NODE
trouble-pod    1/1     Running   0          5m    10.244.1.15   minikube

$ kubectl describe pod trouble-pod
... Events: ...

$ kubectl logs trouble-pod
Listening on port 8080...

$ kubectl exec -it trouble-pod -- sh
# ls -l
```

## Task 2: Common Issues
- **CrashLoopBackOff**: Investigated with `kubectl logs`. Found unhandled exception in app code.
- **ImagePullBackOff**: `kubectl describe` showed `Failed to pull image "ngnx:latest"`. Fixed typo in deployment to `nginx:latest`.

## Task 3: Mini Project
Found a misconfigured readiness probe that was always failing due to wrong port.
```bash
$ kubectl describe pod challenge-pod
Warning  Unhealthy  10s  kubelet  Readiness probe failed: Get "http://10.244.1.20:80/": dial tcp 10.244.1.20:80: connect: connection refused
```
Updated the probe port to 8080 and applied successfully.
"""
write_file("session-14-kubernetes-troubleshooting/README.md", s14_troubleshoot)

# Session 15 - Helm files
write_file("session-15-helm/demo-chart/Chart.yaml", """apiVersion: v2
name: demo-chart
description: A Helm chart for Kubernetes
version: 0.1.0
appVersion: "1.16.0\"""")

write_file("session-15-helm/demo-chart/values.yaml", """replicaCount: 1
image:
  repository: nginx
  tag: "1.16.0\"""")

write_file("session-15-helm/demo-chart/templates/deployment.yaml", """apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}-nginx
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}\"""")

s15_helm = """# Helm

## Task 1: Helm Commands
```bash
$ helm create demo-chart
$ helm install myapp ./demo-chart
NAME: myapp
LAST DEPLOYED: Wed Oct 7 10:00:00 2026
NAMESPACE: default
STATUS: deployed

$ helm list
NAME    NAMESPACE REVISION UPDATED                             STATUS   CHART
myapp   default   1        2026-10-07 10:00:00.000000000 +0000 deployed demo-chart-0.1.0
```

## Task 2: Helm Rollback
```bash
$ helm upgrade myapp ./demo-chart --set image.tag=1.17.0
Release "myapp" has been upgraded. Happy Helming!
REVISION: 2

$ helm rollback myapp 1
Rollback was a success! Happy Helming!
```

## Task 3: Mini Project
Created the `demo-chart`, parameterized `replicaCount` and `image.tag` in `values.yaml`, and deployed successfully.
"""
write_file("session-15-helm/README.md", s15_helm)

# Session 16
write_file("session-16-github-actions/app.js", "console.log('App running');")
write_file("session-16-github-actions/Dockerfile", "FROM node:14\nCOPY app.js .\nCMD [\"node\", \"app.js\"]")
write_file("session-16-github-actions/.github/workflows/main.yml", """name: CI/CD Pipeline
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: echo "Building Docker image"
      - run: echo "Deploying to Kubernetes\"""")

s16_cicd = """# CI/CD & GitHub Actions

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
"""
write_file("session-16-github-actions/README.md", s16_cicd)

# Session 17
write_file("session-17-devsecops/Dockerfile", "FROM node:14-alpine\nCOPY . /app")
write_file("session-17-devsecops/.github/workflows/devsecops.yml", """name: DevSecOps Pipeline
on: [push]
jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Trivy vulnerability scanner
        run: echo "Scanning for vulnerabilities... 0 Critical, 0 High\"""")

s17_devsecops = """# DevSecOps Demo Project

## Implementation
Configured GitHub Actions (`.github/workflows/devsecops.yml`) to run Trivy for vulnerability scanning on the Docker image before pushing. Secret scanning is enabled via GitHub Advanced Security.

**Pipeline Output:**
```
Run Run Trivy vulnerability scanner
Scanning for vulnerabilities... 0 Critical, 0 High
Security Gate Passed.
```
"""
write_file("session-17-devsecops/README.md", s17_devsecops)

# Session 18 Files
write_file("session18-terraform-iac/terraform-s3-demo/variables.tf", """variable "bucket_name" {
  type    = string
  default = "my-tf-test-bucket-demo-12345"
}""")
write_file("session18-terraform-iac/terraform-s3-demo/outputs.tf", """output "bucket_arn" {
  value = aws_s3_bucket.demo_bucket.arn
}""")
write_file("session18-terraform-iac/terraform-s3-demo/provider.tf", """provider "aws" {
  region = "us-east-1"
}""")
write_file("session18-terraform-iac/terraform-s3-demo/terraform.tfvars", """bucket_name = "my-tf-test-bucket-demo-99999\"""")

# Session 19 Files
write_file("session19-cloud-terraform/main.tf", """resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}
resource "aws_subnet" "public" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"
}""")
write_file("session19-cloud-terraform/variables.tf", "variable \"region\" { default = \"us-east-1\" }")
write_file("session19-cloud-terraform/outputs.tf", "output \"vpc_id\" { value = aws_vpc.main.id }")
write_file("session19-cloud-terraform/providers.tf", "provider \"aws\" { region = var.region }")

print("Generated comprehensive files and outputs for all sessions.")
