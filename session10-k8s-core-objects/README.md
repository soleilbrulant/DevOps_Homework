# Kubernetes Pods, ReplicaSets & Deployments

## Task 1: Deployment Strategies
- **Rolling Update**: Default. Updates pods one by one.
- **Blue-Green**: Two identical environments. Switch traffic from old (blue) to new (green).
- **Canary**: Route 5-10% traffic to new version to test, then rollout to all.
- **Recreate**: Kill all old pods, then start new ones. Causes downtime.

## Task 2: Pod Lifecycle
- Pending: Pod accepted but not scheduled or images downloading.
- Running: Bound to a node, containers running.
- Succeeded: All containers terminated successfully.
- Failed: At least one container terminated in failure.
- Unknown: State cannot be obtained.