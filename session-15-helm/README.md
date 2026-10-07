# Helm

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