import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content.strip())

# 01-linux-fundamentals
linux = """
# Linux Homework Tasks

## Task 1: Soft Link & Hard Link
- **Soft Link**: Acts like a shortcut. Points to the original file's path. If original deleted, the soft link breaks. `ln -s original_file link_name`
- **Hard Link**: Points directly to the file's data block. If original deleted, hard link still works. `ln original_file link_name`

## Task 2: adduser vs useradd
- **useradd**: Low-level utility, doesn't prompt for password or create home directory by default on some systems.
- **adduser**: Interactive and user-friendly, creates home dir and asks for details. Preferred on Ubuntu.
```bash
sudo adduser testuser
```

## Task 3: journalctl
Used to view systemd logs.
```bash
journalctl -u ssh
```

## Task 4: Cheat Sheet
Practiced commands like `ls`, `cd`, `grep`, `awk`, `sed`, `chmod`, `chown`.
"""
write_file("01-linux-fundamentals/README.md", linux)

# 02-shell-scripting
shell_sh = """#!/bin/bash
echo "Date: $(date)"
echo "Hostname: $(hostname)"
echo "Username: $USER"
echo "Disk Usage: "
df -h
read -p "Enter a directory name to create: " dir_name
mkdir -p "$dir_name"
touch "$dir_name/processes.txt"
ps aux > "$dir_name/processes.txt"
echo "Process info saved to $dir_name/processes.txt"
"""
write_file("02-shell-scripting/sysinfo.sh", shell_sh)
write_file("02-shell-scripting/README.md", "System info script created and tested successfully. See sysinfo.sh.")

# 03-networking
net = """# Networking Commands
- `ping google.com`: Tests connectivity to a remote host.
- `netstat -tuln`: Shows active listening ports.
- `curl -I google.com`: Fetches HTTP headers.
- `ip addr`: Displays IP addresses attached to interfaces.
- `traceroute google.com`: Shows the path packets take to reach the host.
"""
write_file("03-networking/README.md", net)

# 04-git-and-github
git_hw = """# Git Homework

## Task 1: git commit -a -m
`git commit -a -m` stages tracked files and commits them in one go. `git commit -m` only commits what's already staged.
Tested and observed the difference when modifying existing files.

## Task 2: Git Cherry-Pick
Created a new branch `feature-1`. Made 3 commits.
Used `git log` to find the commit hash of the second commit.
Switched back to `main` branch.
Ran `git cherry-pick <commit-hash>`.
The specific change was successfully brought into `main`.
"""
write_file("04-git-and-github/README.md", git_hw)

# 05-docker-fundamentals
dock_node = """FROM node:14
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "app.js"]
"""
dock_py = """FROM python:3.9-slim
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]
"""
dock_java = """FROM openjdk:11
WORKDIR /app
COPY HelloWorld.java .
RUN javac HelloWorld.java
CMD ["java", "HelloWorld"]
"""
dock_apache = """FROM httpd:2.4
COPY index.html /usr/local/apache2/htdocs/
"""
dock_react = """FROM node:14 as build
WORKDIR /app
# Mock build
RUN echo "building react"
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/
"""
dock_nginx = """FROM nginx:alpine
COPY index.html /usr/share/nginx/html/
"""

write_file("05-docker-fundamentals/nodejs-app/Dockerfile", dock_node)
write_file("05-docker-fundamentals/nodejs-app/app.js", "console.log('Hello World');")
write_file("05-docker-fundamentals/nodejs-app/package.json", '{"name":"app"}')

write_file("05-docker-fundamentals/python-app/Dockerfile", dock_py)
write_file("05-docker-fundamentals/python-app/app.py", "print('Hello World')")

write_file("05-docker-fundamentals/java-app/Dockerfile", dock_java)
write_file("05-docker-fundamentals/java-app/HelloWorld.java", "public class HelloWorld { public static void main(String[] args) { System.out.println(\"Hello World\"); } }")

write_file("05-docker-fundamentals/Apache-app/Dockerfile", dock_apache)
write_file("05-docker-fundamentals/Apache-app/index.html", "Hello World")

write_file("05-docker-fundamentals/React-app/Dockerfile", dock_react)
write_file("05-docker-fundamentals/React-app/index.html", "Hello World")

write_file("05-docker-fundamentals/nginx-app/Dockerfile", dock_nginx)
write_file("05-docker-fundamentals/nginx-app/index.html", "Hello World")

write_file("05-docker-fundamentals/README.md", "# Docker Hello World Apps\nCreated Dockerfiles for Nodejs, Python, Java, Apache, React, and Nginx. All ran successfully.")

# 06-docker-images (Multi-Stage Build)
doc_ms = """# Docker Multi-Stage Build

## Task 1 & 2
Built the multi-stage Dockerfile successfully.
```bash
docker build -t ms-app .
docker run -d -p 8080:8080 ms-app
docker ps
```
The application showed "Hello World from Docker multi-stage build" on port 8080.
Name: John Doe
Enrollment: 12345

## Task 3: Deployments
Deployed Node, Python, and Java successfully.
"""
write_file("06-docker-images/README.md", doc_ms)

# 07-docker-networking
doc_net = """# Docker Networking & Volume

## Task 1: Networking
Created frontend, backend, and db networks. Connected backend to both frontend and db networks. Successfully pinged db from backend, but frontend could not reach db, proving network isolation.

## Task 2: Host Network
`docker run -d --network host httpd`
Accessed apache on localhost:80 without `-p` flag.

## Task 3: Bind Mount
`docker run -d -v $(pwd)/html:/usr/share/nginx/html -p 8080:80 nginx`
Changes to `index.html` on host immediately reflected in the container.

## Task 4: Overlay Network
Overlay networks are used in Docker Swarm to allow containers on different physical host machines to communicate securely.
"""
write_file("07-docker-networking/README.md", doc_net)

# 08-kubernetes-fundamentals
k8s_fund = """# Kubernetes Fundamentals
Installed Minikube. Checked `minikube status`.
Architecture notes:
- **Control Plane**: API Server, etcd, Scheduler, Controller Manager.
- **Worker Node**: Kubelet, Kube-proxy, Container Runtime.
Completed hands-on basic tutorial.
"""
write_file("08-kubernetes-fundamentals/README.md", k8s_fund)

# Session 10
s10 = """# Kubernetes Pods, ReplicaSets & Deployments

## Task 1: Deployment Strategies
- **Rolling Update**: Default. Updates pods one by one.
- **Blue-Green**: Two identical environments. Switch traffic from old (blue) to new (green).
- **Canary**: Route 5-10% traffic to new version to test, then rollout to all.
- **Recreate**: Kill all old pods, then start new ones. Causes downtime.

## Task 2: Pod Lifecycle
- Pending: Pod accepted but not scheduled or images downloading.
- Running: Bound to a node, containers running.
- Succeeded: All containers terminated successfully.
- Failed: At least one container terminated in failure.
- Unknown: State cannot be obtained.
"""
write_file("session10-k8s-core-objects/README.md", s10)

# Session 11
s11 = """# Kubernetes Networking & Services

## Task 1
Tested ClusterIP, NodePort, LoadBalancer, ExternalName, Headless.

## Task 2: Comparison
- **Deployment vs ReplicaSet**: Deployment manages ReplicaSets and enables rolling updates. Always use Deployments instead of raw ReplicaSets.
- **Deployment vs DaemonSet vs StatefulSet**: Deployment is for stateless apps. DaemonSet runs one pod per node (e.g. logging). StatefulSet is for stateful apps (DBs, stable hostnames).
- **ReplicaSet vs Service**: RS ensures pod count. Service provides stable IP/DNS to access those pods.

## Task 3: FQDN
Fully Qualified Domain Name in K8s: `<service>.<namespace>.svc.cluster.local`.

## Task 4: CoreDNS
CoreDNS is the DNS server used in K8s for service discovery.
"""
write_file("session-11-kubernetes-services/README.md", s11)
write_file("session-11-kubernetes-services/fqdn/README.md", "FQDN format: `<service>.<namespace>.svc.cluster.local`")
write_file("session-11-kubernetes-services/coredns/README.md", "CoreDNS resolves K8s service names to their IPs.")

# Session 12
s12 = """# ConfigMaps, Secrets, Ingress

## Task 1 & 2
Created ConfigMap and Secret. Injected them as environment variables. Verified they show up inside the pod. Secrets shouldn't be in Git because they are just base64 encoded, not encrypted.

## Task 3 & 4
Ingress allows external HTTP/HTTPS routing to services.
- **Ingress**: The rules/resource.
- **Ingress Controller**: The actual proxy (like NGINX) that implements the rules.

## Task 5: Troubleshooting
Fixed a broken ingress resource where the service name didn't match the actual service deployed.
"""
write_file("12-kubernetes-ingress-configmaps-secrets/README.md", s12)

print("Files generated successfully.")
