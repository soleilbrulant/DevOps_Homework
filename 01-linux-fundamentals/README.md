# Linux Homework Tasks

## Task 1: Soft Link & Hard Link
- **Soft Link**: Acts like a shortcut. Points to the original file's path. If original deleted, the soft link breaks. `ln -s original_file link_name`
- **Hard Link**: Points directly to the file's data block. If original deleted, hard link still works. `ln original_file link_name`

## Task 2: adduser vs useradd
- **useradd**: Low-level utility, doesn't prompt for password or create home directory by default on some systems.
- **adduser**: Interactive and user-friendly, creates home dir and asks for details. Preferred on Ubuntu.
```bash
sudo adduser testuser
```

## Task 3: journalctl
Used to view systemd logs.
```bash
journalctl -u ssh
```

## Task 4: Cheat Sheet
Practiced commands like `ls`, `cd`, `grep`, `awk`, `sed`, `chmod`, `chown`.