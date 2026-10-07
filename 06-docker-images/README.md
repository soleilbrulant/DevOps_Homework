# Docker Multi-Stage Build

## Task 1 & 2
Built the multi-stage Dockerfile successfully.
```bash
docker build -t ms-app .
docker run -d -p 8080:8080 ms-app
docker ps
```
The application showed "Hello World from Docker multi-stage build" on port 8080.
Name: John Doe
Enrollment: 12345

## Task 3: Deployments
Deployed Node, Python, and Java successfully.