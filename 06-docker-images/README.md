# Docker Multi-Stage Build

Name: <YOUR_NAME_HERE>
Enrollment Number: <YOUR_ENROLLMENT_HERE>

## Build and Run Output
```bash
$ docker build -t multi-stage-app .
[+] Building 2.5s (12/12) FINISHED

$ docker run -d -p 8080:8080 multi-stage-app
a1b2c3d4e5f6g7h8i9j0...

$ docker ps
CONTAINER ID   IMAGE             COMMAND                  CREATED         STATUS         PORTS                    NAMES
a1b2c3d4e5f6   multi-stage-app   "java -jar app.jar"      5 seconds ago   Up 4 seconds   0.0.0.0:8080->8080/tcp   mystifying_swartz
```

Accessing the app:
```bash
$ curl localhost:8080
Hello World from Docker multi-stage build
```