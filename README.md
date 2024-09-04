# Network Printer Scanner

This Python script is designed to scan a local network and identify printers connected to it by detecting open ports associated with printer services. It uses the `nmap` library to scan the network range and provides detailed information about each device found, including its IP address, open ports (631 for IPP and 9100 for JetDirect), and operating system fingerprint when available.

## Features:
- Automatically detects the local network range based on the system's IP address.
- Scans for devices with open printer-specific ports (9100 and 631).
- Provides detailed information on each discovered device, including IP address, open ports, and operating system details.
- Identifies devices using OS fingerprinting to help distinguish printers from other network devices.
- Compatible with networks using a `192.168.x.x` IP range or customizable to other ranges.

## Requirements:
- Python 3.x
- `nmap` library: Install with `pip install python-nmap`
- Nmap must be installed on your system and accessible through the command line.

## How to Use:
1. Install the required Python libraries:
   ```bash
   pip install python-nmap

## Example Output
Local IP: 192.168.2.52
Scanning IP range: 192.168.2.0/24
Starting network scan, please wait...
Printer found: 192.168.2.18 on port 9100, OS: HP LaserJet 2055dn, 2420, P3005, CP4005, 4250, P4014, or P4015 printer
