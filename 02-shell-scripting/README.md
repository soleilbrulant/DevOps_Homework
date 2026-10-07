# Shell Scripting Homework Output

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