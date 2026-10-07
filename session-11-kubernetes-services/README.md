# Kubernetes Networking & Services

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