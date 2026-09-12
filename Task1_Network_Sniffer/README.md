@'
# CodeAlpha Network Sniffer

## Task 1: Basic Network Sniffer

A Python-based network packet sniffer that captures and analyzes network traffic.

## Features
- Real-time packet capture
- Protocol identification (TCP, UDP, ICMP)
- Source/Destination IP display
- Port information
- Payload inspection
- BPF filter support

## Requirements
- Python 3.8+
- Scapy library
- Root/Administrator privileges

## Installation
pip install scapy

## Usage
sudo python3 network_sniffer.py [options]

Options:
  -i, --interface   Network interface
  -c, --count       Packet count (0 = unlimited)
  -f, --filter      BPF filter expression

## Learning Outcomes
- Understanding network protocol structure
- Packet analysis techniques
- Network traffic monitoring
'@ | Out-File -FilePath README.md -Encoding utf8