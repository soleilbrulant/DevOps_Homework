# Kubernetes Troubleshooting

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