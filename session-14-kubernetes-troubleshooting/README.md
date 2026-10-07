# Kubernetes Troubleshooting

## Task 1: Commands
- `kubectl get pods`: Lists pods.
- `kubectl describe pod <name>`: Shows detailed state.
- `kubectl logs <name>`: Gets logs from the container.
- `kubectl exec -it <name> -- sh`: Opens a shell inside the pod.
- `kubectl events`: Shows recent cluster events.
- `kubectl explain <resource>`: Documentation of resource fields.
- `kubectl top pods`: Shows resource usage.
- `kubectl get pods -o wide`: Shows more details like IP and Node.

## Task 2: Common Issues
- **CrashLoopBackOff**: Container keeps crashing. Investigated with `kubectl logs`. Found application error, fixed code, pushed new image.
- **ImagePullBackOff**: Typo in image name. Used `kubectl describe` to see the event. Fixed image name in deployment.
- **Pending**: Insufficient resources on nodes. Checked with `kubectl describe pod`. Scaled up cluster or reduced requests.
- **Service connectivity**: Selector mismatch. Checked endpoint object `kubectl get ep`. Fixed labels.

## Task 3: Mini Project
Troubleshooting challenge completed. Found a misconfigured readiness probe that was always failing due to wrong port, causing the pod to never receive traffic. Updated the probe port to 8080 and applied.
