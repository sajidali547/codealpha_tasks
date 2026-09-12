@'
# CodeAlpha Network Intrusion Detection System

## Task 4: NIDS using Snort

A network-based intrusion detection system using Snort with custom rules and a Python Flask dashboard.

## Features
- Snort IDS with custom rules
- Real-time alert monitoring
- Flask web dashboard
- Detects: ICMP flood, port scans, SSH brute force, suspicious HTTP, FTP brute force

## Setup (Ubuntu / WSL2)

sudo apt update
sudo apt install snort -y
sudo cp /etc/snort/snort.conf /etc/snort/snort.conf.bak
sudo nano /etc/snort/snort.conf
# Uncomment: include $RULE_PATH/local.rules
sudo nano /etc/snort/rules/local.rules
# Paste content of local.rules
sudo snort -T -c /etc/snort/snort.conf
sudo snort -A console -q -c /etc/snort/snort.conf -i eth0

## Run Dashboard

pip install flask
sudo python3 ids_monitor.py
# Open http://localhost:5000
'@ | Out-File -FilePath README.md -Encoding utf8