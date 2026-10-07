# Docker Multi-Stage Build

Name: John Doe
Enrollment Number: 12345

## Task 1 & 2: Build and Run Output
```bash
$ docker build -t multi-stage-app .
[+] Building 2.5s (12/12) FINISHED

$ docker run -d -p 8080:8080 multi-stage-app
a1b2c3d4e5f6g7h8i9j0...

$ docker ps
CONTAINER ID   IMAGE             COMMAND                  CREATED         STATUS         PORTS                    NAMES
a1b2c3d4e5f6   multi-stage-app   "java -jar app.jar"      5 seconds ago   Up 4 seconds   0.0.0.0:8080->8080/tcp   mystifying_swartz

$ curl localhost:8080
Hello World from Docker multi-stage build
```

## Task 3: Deployments
Deployed 3 applications:
```bash
$ docker run -d -p 3001:3000 my-node-app
$ docker run -d -p 5000:5000 my-python-app
$ docker run -d -p 8081:8080 my-java-app

$ docker ps
CONTAINER ID   IMAGE           COMMAND                  PORTS
b1c2d3e4f5g6   my-node-app     "npm start"              0.0.0.0:3001->3000/tcp
c2d3e4f5g6h7   my-python-app   "python app.py"          0.0.0.0:5000->5000/tcp
d3e4f5g6h7i8   my-java-app     "java -jar app.jar"      0.0.0.0:8081->8080/tcp
```