# Monitoring, Observability & GitOps

## Observability Pillars
1. **Metrics**: Numerical representation of data measured over time (e.g., CPU %).
2. **Logs**: Immutable timestamped records of discrete events.
3. **Traces**: Representation of a series of causally related distributed events.

## GitOps
GitOps uses Git repositories as a single source of truth to deliver infrastructure as code.
Tools like ArgoCD continuously monitor the repo and apply the desired state to the cluster.
