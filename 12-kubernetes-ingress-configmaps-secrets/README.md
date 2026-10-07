# ConfigMaps, Secrets, Ingress

## Task 1 & 2
Created ConfigMap and Secret. Injected them as environment variables. Verified they show up inside the pod. Secrets shouldn't be in Git because they are just base64 encoded, not encrypted.

## Task 3 & 4
Ingress allows external HTTP/HTTPS routing to services.
- **Ingress**: The rules/resource.
- **Ingress Controller**: The actual proxy (like NGINX) that implements the rules.

## Task 5: Troubleshooting
Fixed a broken ingress resource where the service name didn't match the actual service deployed.