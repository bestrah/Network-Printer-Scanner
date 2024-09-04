import nmap
import socket
import time

def scan_network():
    # تنظیم محدوده آی‌پی بر اساس default gateway
    ip_range = '192.168.2.0/24'
    
    print(f"Scanning IP range: {ip_range}")
    
    # استفاده از nmap برای اسکن شبکه
    nm = nmap.PortScanner()
    print("Starting network scan, please wait...")
    
    # اسکن محدوده شبکه برای پورت‌های مرتبط با پرینترها
    nm.scan(ip_range, '9100,631', arguments='-O')  # اسکن با فعال کردن OS detection
    
    # بررسی دستگاه‌ها و پورت‌های باز
    found_printers = []
    for host in nm.all_hosts():
        if 'tcp' in nm[host]:
            for port in nm[host]['tcp']:
                # بررسی پورت 9100 و 631 که پرینترها استفاده می‌کنند
                if port == 9100 or port == 631:
                    # دریافت اطلاعات دستگاه
                    try:
                        os = nm[host]['osmatch'][0]['name']
                    except:
                        os = 'Unknown OS'
                    
                    print(f"Printer found: {host} on port {port}, OS: {os}")
                    found_printers.append((host, port, os))
    
    if not found_printers:
        print("No printers found on the network.")
    else:
        print(f"{len(found_printers)} printer(s) found.")

if __name__ == "__main__":
    scan_network()
    time.sleep(2)
