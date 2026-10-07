# Linux Homework Tasks

## Task 1: Soft Link & Hard Link
```bash
$ echo "hello" > original.txt
$ ln -s original.txt softlink.txt
$ ln original.txt hardlink.txt
$ ls -l
-rw-r--r-- 2 student student 6 Oct  7 10:00 hardlink.txt
-rw-r--r-- 2 student student 6 Oct  7 10:00 original.txt
lrwxrwxrwx 1 student student 12 Oct  7 10:00 softlink.txt -> original.txt
```
- **Soft Link**: Acts like a shortcut. If original deleted, the soft link breaks.
- **Hard Link**: Points directly to the file's data block. If original deleted, hard link still works.

## Task 2: adduser vs useradd
- **useradd**: Low-level utility, doesn't prompt for password or create home directory by default on some systems.
- **adduser**: Interactive and user-friendly, creates home dir and asks for details. Preferred on Ubuntu.
```bash
$ sudo adduser testuser
Adding user `testuser' ...
Adding new group `testuser' (1001) ...
Adding new user `testuser' (1001) with group `testuser' ...
Creating home directory `/home/testuser' ...
Copying files from `/etc/skel' ...
New password: 
```

## Task 3: journalctl
Used to view systemd logs.
```bash
$ sudo journalctl -u ssh -n 5
Oct 07 10:01:00 server sshd[123]: Accepted publickey for user
Oct 07 10:01:01 server sshd[123]: pam_unix(sshd:session): session opened for user
```

## Task 4: Cheat Sheet
Practiced basic commands.
```bash
$ ls -la
$ chmod 755 script.sh
$ grep "error" /var/log/syslog
```