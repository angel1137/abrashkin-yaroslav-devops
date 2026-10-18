
#!/bin/bash

echo "=============================="
echo "Student Information"
echo "=============================="
echo "Name: Yaroslav"
echo "Surname: Abrashkin"
echo "Group: IT2-2304"
echo "Student ID: 37035"

echo "=============================="
echo "System Information"
echo "=============================="
echo "Username: $(whoami)"
echo "Hostname: $(hostname)"
echo "Current Date: $(date)"
echo "Operating System: $(uname -a)"
echo "Disk Usage:"
df -h /
echo "Memory Usage:"
free -h

if [ -f "$HOME/devops/abrashkin_yaroslav/Abrashkin_Yaroslav_info.txt" ]; then
    echo "Student information file exists."
else
    echo "Student information file does not exist."
fi
