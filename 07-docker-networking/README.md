# Docker Networking & Volume

## Task 1: Container Networking
```bash
$ docker network create frontend
$ docker network create backend
$ docker network create db_net

$ docker run -d --name web --network frontend nginx:alpine
$ docker run -d --name api --network backend alpine sleep 3600
$ docker run -d --name db --network db_net mysql:8.0

$ docker network connect backend web
$ docker network connect backend db

$ docker exec -it api ping -c 2 db
PING db (172.19.0.3): 56 data bytes
64 bytes from 172.19.0.3: seq=0 ttl=64 time=0.150 ms
```
Connectivity between `api` and `db` works because they are both on the backend network.

## Task 2: Host Network
```bash
$ docker run -d --network host httpd
$ curl localhost:80
<html><body><h1>It works!</h1></body></html>
```

## Task 3: Bind Mount
```bash
$ mkdir html && echo "Hello students" > html/index.html
$ docker run -d -v $(pwd)/html:/usr/share/nginx/html -p 8080:80 nginx
$ curl localhost:8080
Hello students

$ echo "Modified" > html/index.html
$ curl localhost:8080
Modified
```
Changes reflected immediately without restarting.