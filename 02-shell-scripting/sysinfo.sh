#!/bin/bash
echo "Date: $(date)"
echo "Hostname: $(hostname)"
echo "Username: $USER"
echo "Disk Usage: "
df -h
read -p "Enter a directory name to create: " dir_name
mkdir -p "$dir_name"
touch "$dir_name/processes.txt"
ps aux > "$dir_name/processes.txt"
echo "Process info saved to $dir_name/processes.txt"