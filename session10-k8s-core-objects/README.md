# Kubernetes Pods, ReplicaSets & Deployments

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