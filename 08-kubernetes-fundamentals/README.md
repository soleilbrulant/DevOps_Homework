# Kubernetes Fundamentals

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