# Helm

## Task 1: Helm Commands
- `helm create mychart`: Creates a boilerplate chart.
- `helm install myapp ./mychart`: Installs the chart.
- `helm list`: Lists installed releases.
- `helm status myapp`: Shows release status.
- `helm upgrade myapp ./mychart`: Upgrades release to new version.
- `helm history myapp`: Shows revision history.
- `helm rollback myapp 1`: Rolls back to revision 1.

## Task 2: Helm Rollback
```bash
$ helm install demo ./demo-chart
NAME: demo
REVISION: 1

$ helm upgrade demo ./demo-chart --set image.tag=v2
Release "demo" has been upgraded.
REVISION: 2

$ helm rollback demo 1
Rollback was a success! Happy Helming!
```

## Task 3: Mini Project
Created a helm chart for a nodejs app, parameterized the replica count and image tag in `values.yaml`, and successfully installed it.
