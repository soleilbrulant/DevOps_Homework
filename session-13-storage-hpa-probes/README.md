# HPA Hands-on and Mini Project

## HPA Setup
Deployed the application and configured HPA:
`kubectl autoscale deployment hpa-example --cpu-percent=50 --min=1 --max=10`

Outputs:
```
$ kubectl get hpa
NAME          REFERENCE                TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
hpa-example   Deployment/hpa-example   0%/50%    1         10        1          2m

$ kubectl top pods
NAME                           CPU(cores)   MEMORY(bytes)
hpa-example-5b9c5f8b9-x7x2m   1m           12Mi
```

After running load generator:
```
$ kubectl get hpa
NAME          REFERENCE                TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
hpa-example   Deployment/hpa-example   250%/50%  1         10        5          5m
```

## Mini Project
Completed the Session 13 mini project involving setting up a PVC for a web app and implementing readiness/liveness probes. The probes successfully detected when the pod was unready and restarted it when liveness failed.
