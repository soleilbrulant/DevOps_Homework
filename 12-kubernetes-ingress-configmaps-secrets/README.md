# ConfigMaps, Secrets, Ingress

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