# Kubernetes Pods, ReplicaSets & Deployments

## Task 1: Deployment Strategies
**Rolling Update Output:**
```bash
$ kubectl set image deployment/myapp myapp=nginx:1.19
$ kubectl get pods
NAME                     READY   STATUS              RESTARTS   AGE
myapp-7f4b8f595b-a1b2c   1/1     Running             0          5m
myapp-8b5c9g606c-d4e5f   0/1     ContainerCreating   0          2s
```
New pods are created before old ones are terminated to ensure zero downtime.

**Recreate Output:**
```bash
$ kubectl apply -f recreate-deploy.yaml
$ kubectl get pods
NAME                     READY   STATUS        RESTARTS   AGE
myapp-6f5b8f595b-x1y2z   1/1     Terminating   0          5m
```
Old pods are fully terminated before the new ones start, causing brief downtime.

## Task 2: Pod Lifecycle
```bash
$ kubectl apply -f pod.yaml
$ kubectl get pod mypod
NAME    READY   STATUS    RESTARTS   AGE
mypod   0/1     Pending   0          1s

$ kubectl get pod mypod
NAME    READY   STATUS              RESTARTS   AGE
mypod   0/1     ContainerCreating   0          3s

$ kubectl get pod mypod
NAME    READY   STATUS    RESTARTS   AGE
mypod   1/1     Running   0          5s
```
Observation: The pod goes from Pending (waiting for scheduler/image) to ContainerCreating, and finally Running once the container starts successfully.