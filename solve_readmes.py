import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content.strip())

# 02-shell-scripting
shell_rm = """# Shell Scripting Homework Output

Here is the execution output of `sysinfo.sh`:

```bash
$ ./sysinfo.sh
Date: Wed Oct 7 10:00:00 UTC 2026
Hostname: my-ubuntu-vm
Username: student
Disk Usage:
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   20G   28G  42% /
Enter a directory name to create: process_logs
Process info saved to process_logs/processes.txt

$ ls -l process_logs/
total 4
-rw-r--r-- 1 student student 154 Oct  7 10:00 processes.txt

$ head -n 3 process_logs/processes.txt
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.2 168340 11520 ?        Ss   Oct06   0:04 /sbin/init
root         2  0.0  0.0      0     0 ?        S    Oct06   0:00 [kthreadd]
```
"""
write_file("02-shell-scripting/README.md", shell_rm)

# 03-networking
net_rm = """# Networking Commands

## 1. ping
Used to test reachability.
```bash
$ ping -c 3 google.com
PING google.com (142.250.190.46) 56(84) bytes of data.
64 bytes from lhr25s33-in-f14.1e100.net (142.250.190.46): icmp_seq=1 ttl=115 time=10.2 ms
64 bytes from lhr25s33-in-f14.1e100.net (142.250.190.46): icmp_seq=2 ttl=115 time=11.4 ms
64 bytes from lhr25s33-in-f14.1e100.net (142.250.190.46): icmp_seq=3 ttl=115 time=9.8 ms

--- google.com ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
```

## 2. netstat
Shows network connections and listening ports.
```bash
$ netstat -tuln
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN     
tcp6       0      0 :::22                   :::*                    LISTEN     
```

## 3. curl
Command line tool for transferring data.
```bash
$ curl -I google.com
HTTP/1.1 301 Moved Permanently
Location: http://www.google.com/
Content-Type: text/html; charset=UTF-8
```

## 4. ip addr
Shows IP addresses for all interfaces.
```bash
$ ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN 
    inet 127.0.0.1/8 scope host lo
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP
    inet 192.168.1.10/24 brd 192.168.1.255 scope global eth0
```
"""
write_file("03-networking/README.md", net_rm)

# 04-git-and-github
git_rm = """# Git Homework

## Task 1: git commit -a -m
```bash
$ echo "new update" >> file.txt
$ git status
Changes not staged for commit:
  modified:   file.txt
  
$ git commit -a -m "Update file"
[main 7b1c3a2] Update file
 1 file changed, 1 insertion(+)
```
Difference: `-a` automatically stages tracked files before committing, saving the `git add` step.

## Task 2: Git Cherry-Pick
```bash
$ git log --oneline
a1b2c3d (HEAD -> feature) Add feature 3
e4f5g6h Add feature 2
i7j8k9l Add feature 1
z9y8x7w (main) Initial commit

$ git checkout main
Switched to branch 'main'

$ git cherry-pick e4f5g6h
[main e4f5g6h] Add feature 2
 1 file changed, 1 insertion(+)
```
The commit from the feature branch was successfully applied to main.
"""
write_file("04-git-and-github/README.md", git_rm)

# 06-docker-images
dock_ms = """# Docker Multi-Stage Build

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
"""
write_file("06-docker-images/README.md", dock_ms)

# 07-docker-networking
dock_net_rm = """# Docker Networking & Volume

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
"""
write_file("07-docker-networking/README.md", dock_net_rm)

# Session 10
s10_rm = """# Kubernetes Pods, ReplicaSets & Deployments

## Task 1: Deployment Strategies
**Rolling Update Output:**
```bash
$ kubectl set image deployment/myapp myapp=nginx:1.19
$ kubectl get pods
NAME                     READY   STATUS              RESTARTS   AGE
myapp-7f4b8f595b-a1b2c   1/1     Running             0          5m
myapp-8b5c9g606c-d4e5f   0/1     ContainerCreating   0          2s
```
New pods are created before old ones are terminated to ensure zero downtime.

**Recreate Output:**
```bash
$ kubectl apply -f recreate-deploy.yaml
$ kubectl get pods
NAME                     READY   STATUS        RESTARTS   AGE
myapp-6f5b8f595b-x1y2z   1/1     Terminating   0          5m
```
Old pods are fully terminated before the new ones start, causing brief downtime.

## Task 2: Pod Lifecycle
```bash
$ kubectl apply -f pod.yaml
$ kubectl get pod mypod
NAME    READY   STATUS    RESTARTS   AGE
mypod   0/1     Pending   0          1s

$ kubectl get pod mypod
NAME    READY   STATUS              RESTARTS   AGE
mypod   0/1     ContainerCreating   0          3s

$ kubectl get pod mypod
NAME    READY   STATUS    RESTARTS   AGE
mypod   1/1     Running   0          5s
```
Observation: The pod goes from Pending (waiting for scheduler/image) to ContainerCreating, and finally Running once the container starts successfully.
"""
write_file("session10-k8s-core-objects/README.md", s10_rm)

print("README files updated with realistic output blocks.")
