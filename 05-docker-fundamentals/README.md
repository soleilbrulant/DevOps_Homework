# Docker Hello World Apps

## Node.js App
```bash
$ docker build -t hello-node ./nodejs-app
$ docker run -d -p 3000:3000 hello-node
```

## Python App
```bash
$ docker build -t hello-python ./python-app
$ docker run -d hello-python
Hello World
```

## Java App
```bash
$ docker build -t hello-java ./java-app
$ docker run --rm hello-java
Hello World
```

## Apache App
```bash
$ docker build -t hello-apache ./Apache-app
$ docker run -d -p 8081:80 hello-apache
```

## React & Nginx Apps
```bash
$ docker build -t hello-react ./React-app
$ docker build -t hello-nginx ./nginx-app
$ docker run -d -p 8082:80 hello-nginx
```
All Dockerfiles created and successfully verified.