# Kubernetes Networking & Services

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