#!/usr/bin/env python3
"""
CodeAlpha Cyber Security Internship
Task 1: Basic Network Sniffer
"""

from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime
import argparse
import sys

class NetworkSniffer:
    def __init__(self, interface=None, count=0, filter_rule=None):
        self.interface = interface
        self.count = count
        self.filter_rule = filter_rule
        self.packet_count = 0

    def get_protocol_name(self, packet):
        if packet.haslayer(TCP): return "TCP"
        elif packet.haslayer(UDP): return "UDP"
        elif packet.haslayer(ICMP): return "ICMP"
        elif packet.haslayer(IP): return "IP"
        return "Unknown"

    def get_payload(self, packet, max_length=100):
        if packet.haslayer(Raw):
            payload = packet[Raw].load
            try:
                decoded = payload.decode('utf-8', errors='ignore')
                return decoded[:max_length] + "..." if len(decoded) > max_length else decoded
            except:
                return str(payload[:max_length])
        return "No payload"

    def analyze_packet(self, packet):
        self.packet_count += 1
        print("\n" + "="*70)
        print(f"PACKET #{self.packet_count}")
        print("="*70)
        print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

        if packet.haslayer(IP):
            ip_layer = packet[IP]
            print(f"\n[IP Layer]")
            print(f"  Source IP:      {ip_layer.src}")
            print(f"  Destination IP: {ip_layer.dst}")
            print(f"  TTL:            {ip_layer.ttl}")
            print(f"  Protocol:       {self.get_protocol_name(packet)}")

            if packet.haslayer(TCP):
                tcp = packet[TCP]
                print(f"\n[TCP Layer]")
                print(f"  Source Port:      {tcp.sport}")
                print(f"  Destination Port: {tcp.dport}")
                print(f"  Flags:            {tcp.flags}")
                print(f"  Sequence:         {tcp.seq}")
            elif packet.haslayer(UDP):
                udp = packet[UDP]
                print(f"\n[UDP Layer]")
                print(f"  Source Port:      {udp.sport}")
                print(f"  Destination Port: {udp.dport}")
                print(f"  Length:           {udp.len}")
            elif packet.haslayer(ICMP):
                icmp = packet[ICMP]
                print(f"\n[ICMP Layer]")
                print(f"  Type: {icmp.type}")
                print(f"  Code: {icmp.code}")

            payload = self.get_payload(packet)
            if payload != "No payload":
                print(f"\n[Payload]\n  {payload}")
        else:
            print("  Non-IP packet captured")

    def start_capture(self):
        print("\n" + "="*70)
        print("       CODEALPHA NETWORK SNIFFER")
        print("="*70)
        print(f"Interface: {self.interface or 'Default'}")
        print(f"Packet Count: {self.count if self.count > 0 else 'Unlimited'}")
        print(f"Filter: {self.filter_rule or 'None'}")
        print("="*70)
        print("\nStarting capture... Press Ctrl+C to stop\n")
        try:
            sniff(
                iface=self.interface,
                count=self.count if self.count > 0 else 0,
                filter=self.filter_rule,
                prn=self.analyze_packet,
                store=False
            )
        except KeyboardInterrupt:
            print("\n\n[!] Capture stopped by user")
        except PermissionError:
            print("\n[!] Error: Run with sudo/administrator privileges")
            sys.exit(1)
        finally:
            print(f"\n{'='*70}")
            print(f"CAPTURE SUMMARY — Total packets: {self.packet_count}")

def main():
    parser = argparse.ArgumentParser(description='CodeAlpha Network Sniffer')
    parser.add_argument('-i', '--interface', help='Network interface')
    parser.add_argument('-c', '--count', type=int, default=0, help='Number of packets')
    parser.add_argument('-f', '--filter', help='BPF filter')
    args = parser.parse_args()
    sniffer = NetworkSniffer(args.interface, args.count, args.filter)
    sniffer.start_capture()

if __name__ == "__main__":
    main()