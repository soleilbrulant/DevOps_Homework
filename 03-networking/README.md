# Networking Commands

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