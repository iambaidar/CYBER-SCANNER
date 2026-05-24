#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================
#   CYBER.IR - Network Intelligence & Reconnaissance Tool
#   Created By: BAIDAR
#   For: Termux / Linux Environment
# ============================================================

import os
import sys
import time
import socket
import threading
import subprocess
import re
from datetime import datetime

# All RED colors for Termux
R = "\033[91m"      # Bright Red
DR = "\033[31m"     # Dark Red
BOLD = "\033[1m"
D = "\033[0m"

def banner():
    os.system('clear')
    print(f"""
{BOLD}{R}
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║   ██████╗██╗   ██╗██████╗ ███████╗██████╗    ██╗██████╗     ║
    ║  ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗   ██║██╔══██╗    ║
    ║  ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝   ██║██████╔╝    ║
    ║  ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗   ██║██╔══██╗    ║
    ║  ╚██████╗   ██║   ██████╔╝███████╗██║  ██║██╗██║██║  ██║    ║
    ║   ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝╚═╝╚═╝  ╚═╝    ║
    ║                                                              ║
    ║              NETWORK INTELLIGENCE & RECONNAISSANCE           ║
    ║                                                              ║
    ║                    CREATED BY BAIDAR                         ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
{D}
    """)

def print_status(msg):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"{R}[{timestamp}] {msg}{D}")

def print_section(title):
    print(f"\n{BOLD}{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{D}")
    print(f"{BOLD}{R}  ► {title}{D}")
    print(f"{BOLD}{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{D}\n")

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def get_network_range():
    ip = get_local_ip()
    parts = ip.split('.')
    return f"{parts[0]}.{parts[1]}.{parts[2]}.0/24"

def ping_host(ip):
    try:
        result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=3)
        return result.returncode == 0
    except:
        return False

def scan_ip_range(network_range):
    print_section("NETWORK DISCOVERY - IP SCANNING")
    base_ip = network_range.rsplit('.', 1)[0]
    alive_hosts = []
    print_status(f"Scanning Network: {network_range}")
    print_status(f"Local IP: {get_local_ip()}")
    print_status("Pinging hosts (1-254)... Please wait...\n")
    
    threads = []
    results = {}
    
    def scan_single(ip):
        if ping_host(ip):
            results[ip] = True
    
    for i in range(1, 255):
        ip = f"{base_ip}.{i}"
        t = threading.Thread(target=scan_single, args=(ip,))
        threads.append(t)
        t.start()
        if len(threads) >= 50:
            for t in threads:
                t.join()
            threads = []
    
    for t in threads:
        t.join()
    
    alive_hosts = list(results.keys())
    print(f"{BOLD}{R}╔══════════════════════════════════════════════════════════════╗{D}")
    print(f"{BOLD}{R}║           ALIVE HOSTS FOUND: {len(alive_hosts)}                          ║{D}")
    print(f"{BOLD}{R}╚══════════════════════════════════════════════════════════════╝{D}\n")
    
    for ip in sorted(alive_hosts):
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except:
            hostname = "Unknown"
        device_type = identify_device(ip)
        print(f"  {R}● {ip:<16} | {hostname:<25} | {device_type}{D}")
    
    return alive_hosts

def identify_device(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0].lower()
        if any(x in hostname for x in ['cam', 'dahua', 'hik', 'cctv', 'dvr', 'nvr', 'ipcam']):
            return f"{BOLD}{R}[CCTV/CAMERA]{D}"
        elif any(x in hostname for x in ['router', 'gateway', 'tplink', 'asus', 'netgear']):
            return f"{R}[ROUTER]{D}"
        elif any(x in hostname for x in ['phone', 'android', 'iphone', 'mobile']):
            return f"{R}[MOBILE DEVICE]{D}"
        elif any(x in hostname for x in ['pc', 'desktop', 'laptop', 'notebook']):
            return f"{R}[COMPUTER]{D}"
        elif any(x in hostname for x in ['printer', 'print']):
            return f"{R}[PRINTER]{D}"
        elif any(x in hostname for x in ['tv', 'smarttv', 'samsung']):
            return f"{R}[SMART TV]{D}"
        else:
            return f"{R}[UNKNOWN DEVICE]{D}"
    except:
        return f"{R}[UNKNOWN]{D}"

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except:
        return False

def get_service_name(port):
    common_ports = {
        21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP', 53: 'DNS',
        80: 'HTTP', 110: 'POP3', 135: 'MSRPC', 139: 'NetBIOS', 143: 'IMAP',
        443: 'HTTPS', 445: 'SMB', 993: 'IMAPS', 995: 'POP3S',
        1723: 'PPTP', 3306: 'MySQL', 3389: 'RDP', 5432: 'PostgreSQL',
        5900: 'VNC', 8080: 'HTTP-Proxy', 8443: 'HTTPS-Alt',
        554: 'RTSP', 8554: 'RTSP-Alt', 37777: 'Dahua', 34567: 'Hikvision',
        8000: 'DVR', 9000: 'DVR-Alt', 10554: 'CCTV-Stream'
    }
    return common_ports.get(port, 'Unknown')

def scan_ports(ip, ports=None):
    if ports is None:
        ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 
                 443, 445, 554, 993, 995, 1723, 3306, 3389, 
                 5432, 5900, 8000, 8080, 8443, 8554, 9000, 
                 10554, 34567, 37777]
    open_ports = []
    for port in ports:
        if scan_port(ip, port):
            service = get_service_name(port)
            open_ports.append((port, service))
    return open_ports

def full_port_scan(alive_hosts):
    print_section("PORT SCANNING - ALL ALIVE HOSTS")
    all_results = {}
    for ip in alive_hosts:
        print_status(f"Scanning ports on {ip}...")
        open_ports = scan_ports(ip)
        all_results[ip] = open_ports
        if open_ports:
            print(f"  {R}✓ {ip} - Open Ports:{D}")
            for port, service in open_ports:
                if port in [554, 8554, 37777, 34567, 8000, 9000, 10554]:
                    print(f"      {BOLD}{R}⚠ {port}/tcp  OPEN  → {service} [POTENTIAL CCTV/DVR]{D}")
                elif port in [80, 443, 8080, 8443]:
                    print(f"      {R}→ {port}/tcp  OPEN  → {service} [Web Interface]{D}")
                else:
                    print(f"      {R}→ {port}/tcp  OPEN  → {service}{D}")
        else:
            print(f"  {R}✗ {ip} - No common ports open{D}")
        print()
    return all_results

def analyze_traffic():
    print_section("NETWORK TRAFFIC ANALYSIS")
    print_status("Analyzing network traffic...")
    print_status("Capturing packets for 15 seconds...\n")
    try:
        result = subprocess.run(['tcpdump', '-i', 'any', '-n', '-c', '500', '-q'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=20, text=True)
        traffic_data = {}
        if result.returncode == 0 or result.stdout:
            lines = result.stdout.split('\n')
            for line in lines:
                ip_pattern = r'(\d+\.\d+\.\d+\.\d+)'
                ips = re.findall(ip_pattern, line)
                for ip in ips:
                    if ip not in traffic_data:
                        traffic_data[ip] = {'packets': 0, 'bytes': 0}
                    traffic_data[ip]['packets'] += 1
                    byte_match = re.search(r'length (\d+)', line)
                    if byte_match:
                        traffic_data[ip]['bytes'] += int(byte_match.group(1))
        
        if not traffic_data:
            result2 = subprocess.run(['netstat', '-tn'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5, text=True)
            if result2.returncode == 0:
                lines = result2.stdout.split('\n')
                for line in lines[2:]:
                    parts = line.split()
                    if len(parts) >= 5:
                        remote = parts[4]
                        if ':' in remote:
                            ip = remote.rsplit(':', 1)[0]
                            if ip not in traffic_data:
                                traffic_data[ip] = {'packets': 0, 'bytes': 0}
                            traffic_data[ip]['packets'] += 1
        
        sorted_traffic = sorted(traffic_data.items(), key=lambda x: x[1]['packets'], reverse=True)
        print(f"{BOLD}{R}╔══════════════════════════════════════════════════════════════╗{D}")
        print(f"{BOLD}{R}║              TOP TRAFFIC SOURCES/DESTINATIONS                ║{D}")
        print(f"{BOLD}{R}╚══════════════════════════════════════════════════════════════╝{D}\n")
        print(f"  {BOLD}{R}{'Rank':<6}{'IP Address':<18}{'Packets':<12}{'Est. Data':<15}{D}")
        print(f"  {R}{'-'*55}{D}")
        
        for idx, (ip, data) in enumerate(sorted_traffic[:15], 1):
            packets = data['packets']
            bytes_total = data['bytes']
            if bytes_total > 1024*1024:
                data_size = f"{bytes_total/(1024*1024):.2f} MB"
            elif bytes_total > 1024:
                data_size = f"{bytes_total/1024:.2f} KB"
            else:
                data_size = f"{bytes_total} B"
            
            if idx == 1:
                indicator = "🔥"
            elif idx <= 3:
                indicator = "⚡"
            else:
                indicator = "•"
            print(f"  {R}{indicator} #{idx:<4}{ip:<18}{packets:<12}{data_size:<15}{D}")
        
        if sorted_traffic:
            top_ip = sorted_traffic[0][0]
            top_packets = sorted_traffic[0][1]['packets']
            print(f"\n{BOLD}{R}  🎯 HIGHEST TRAFFIC IP: {top_ip} ({top_packets} packets){D}")
    except FileNotFoundError:
        print_status("tcpdump not found. Install with: pkg install tcpdump")
    except Exception as e:
        print_status(f"Traffic analysis error: {e}")

def detect_cctv_devices(alive_hosts, port_results):
    print_section("CCTV / DVR / NVR DETECTION")
    cctv_ports = [554, 8554, 37777, 34567, 8000, 9000, 10554, 80, 443, 8080]
    cctv_devices = []
    for ip in alive_hosts:
        is_cctv = False
        detected_ports = []
        try:
            hostname = socket.gethostbyaddr(ip)[0].lower()
            if any(x in hostname for x in ['cam', 'dahua', 'hik', 'cctv', 'dvr', 'nvr', 'ipcam']):
                is_cctv = True
        except:
            pass
        if ip in port_results:
            for port, service in port_results[ip]:
                if port in cctv_ports:
                    is_cctv = True
                    detected_ports.append((port, service))
        if is_cctv:
            cctv_devices.append({'ip': ip, 'ports': detected_ports, 'type': 'CCTV/DVR/NVR'})
    
    if cctv_devices:
        print(f"{BOLD}{R}╔══════════════════════════════════════════════════════════════╗{D}")
        print(f"{BOLD}{R}║         ⚠ CCTV / DVR / NVR DEVICES DETECTED!               ║{D}")
        print(f"{BOLD}{R}╚══════════════════════════════════════════════════════════════╝{D}\n")
        for device in cctv_devices:
            print(f"  {BOLD}{R}📹 {device['ip']}{D}")
            print(f"     {R}Type: {device['type']}{D}")
            if device['ports']:
                print(f"     {R}Open Ports:{D}")
                for port, service in device['ports']:
                    print(f"       {BOLD}{R}→ {port}/tcp  [{service}]{D}")
            print()
        print(f"{R}Total CCTV/DVR Devices Found: {len(cctv_devices)}{D}\n")
    else:
        print(f"{R}✓ No CCTV/DVR/NVR devices detected on this network.{D}\n")
    return cctv_devices

def enumerate_devices(alive_hosts):
    print_section("COMPLETE DEVICE ENUMERATION")
    devices = []
    for ip in alive_hosts:
        device_info = {'ip': ip, 'hostname': 'Unknown', 'mac': 'Unknown', 'type': 'Unknown'}
        try:
            device_info['hostname'] = socket.gethostbyaddr(ip)[0]
        except:
            pass
        try:
            result = subprocess.run(['ip', 'neigh', 'show', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=2, text=True)
            if result.returncode == 0:
                mac_match = re.search(r'([0-9a-fA-F:]{17})', result.stdout)
                if mac_match:
                    device_info['mac'] = mac_match.group(1)
        except:
            pass
        device_info['type'] = identify_device(ip).replace('\033[91m', '').replace('\033[31m', '').replace('\033[1m', '').replace('\033[0m', '').strip('[]')
        devices.append(device_info)
    
    print(f"  {BOLD}{R}{'IP Address':<16}{'Hostname':<25}{'MAC Address':<20}{'Type':<20}{D}")
    print(f"  {R}{'-'*85}{D}")
    for dev in devices:
        print(f"  {R}{dev['ip']:<16}{dev['hostname']:<25}{dev['mac']:<20}{dev['type']:<20}{D}")
    return devices

def show_report_on_screen(alive_hosts, port_results, devices, cctv_devices):
    """Show complete report on screen instead of saving to file"""
    print_section("COMPLETE SCAN REPORT - ON SCREEN")
    
    print(f"{BOLD}{R}╔══════════════════════════════════════════════════════════════╗{D}")
    print(f"{BOLD}{R}║           CYBER.IR - NETWORK INTELLIGENCE REPORT             ║{D}")
    print(f"{BOLD}{R}║                    Created By: BAIDAR                        ║{D}")
    print(f"{BOLD}{R}║           {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}                            ║{D}")
    print(f"{BOLD}{R}╚══════════════════════════════════════════════════════════════╝{D}\n")
    
    print(f"{R}NETWORK RANGE: {get_network_range()}{D}")
    print(f"{R}LOCAL IP: {get_local_ip()}{D}")
    print(f"{R}TOTAL ALIVE HOSTS: {len(alive_hosts)}{D}\n")
    
    print(f"{BOLD}{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{D}")
    print(f"{BOLD}{R}  ALIVE HOSTS{D}")
    print(f"{BOLD}{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{D}\n")
    for ip in sorted(alive_hosts):
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except:
            hostname = "Unknown"
        print(f"  {R}• {ip:<16} | {hostname}{D}")
    
    print(f"\n{BOLD}{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{D}")
    print(f"{BOLD}{R}  OPEN PORTS{D}")
    print(f"{BOLD}{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{D}\n")
    for ip, ports in port_results.items():
        if ports:
            print(f"  {BOLD}{R}{ip}:{D}")
            for port, service in ports:
                print(f"    {R}→ {port}/tcp - {service}{D}")
    
    print(f"\n{BOLD}{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{D}")
    print(f"{BOLD}{R}  CCTV/DVR DEVICES{D}")
    print(f"{BOLD}{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{D}\n")
    if cctv_devices:
        for dev in cctv_devices:
            print(f"  {BOLD}{R}📹 {dev['ip']} - {dev['type']}{D}")
    else:
        print(f"  {R}None detected{D}")
    
    print(f"\n{BOLD}{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{D}")
    print(f"{BOLD}{R}  DEVICE ENUMERATION{D}")
    print(f"{BOLD}{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{D}\n")
    print(f"  {BOLD}{R}{'IP Address':<16}{'Hostname':<25}{'MAC Address':<20}{'Type':<20}{D}")
    print(f"  {R}{'-'*85}{D}")
    for dev in devices:
        print(f"  {R}{dev['ip']:<16}{dev['hostname']:<25}{dev['mac']:<20}{dev['type']:<20}{D}")
    
    print(f"\n{BOLD}{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{D}")
    print(f"{BOLD}{R}                    END OF REPORT{D}")
    print(f"{BOLD}{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{D}\n")

def check_command_exists(cmd):
    try:
        subprocess.run([cmd, '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=2)
        return True
    except FileNotFoundError:
        return False
    except:
        return True

def main():
    banner()
    print(f"{R}  [+] Initializing CYBER.IR Network Scanner...{D}")
    print(f"{R}  [+] Detecting network configuration...{D}")
    time.sleep(1)
    print_status("Checking dependencies...")
    
    deps = {'ping': 'ping', 'python': 'python3'}
    missing = []
    for dep_name, dep_cmd in deps.items():
        if not check_command_exists(dep_cmd):
            missing.append(dep_name)
    
    if missing:
        print_status(f"Missing: {', '.join(missing)}. Install with: pkg install {' '.join(missing)}")
    
    local_ip = get_local_ip()
    network_range = get_network_range()
    print_status(f"Local IP: {local_ip}")
    print_status(f"Network Range: {network_range}")
    
    input(f"\n{R}Press ENTER to start full network scan...{D}")
    
    alive_hosts = scan_ip_range(network_range)
    if not alive_hosts:
        print_status("No alive hosts found! Check your network connection.")
        sys.exit(1)
    time.sleep(1)
    
    port_results = full_port_scan(alive_hosts)
    time.sleep(1)
    
    try:
        analyze_traffic()
    except KeyboardInterrupt:
        print("\n")
        print_status("Traffic analysis interrupted by user.")
    time.sleep(1)
    
    cctv_devices = detect_cctv_devices(alive_hosts, port_results)
    time.sleep(1)
    
    devices = enumerate_devices(alive_hosts)
    
    # Show report on screen instead of saving file
    show_report_on_screen(alive_hosts, port_results, devices, cctv_devices)
    
    print_section("SCAN COMPLETE - SUMMARY")
    print(f"""
    {BOLD}{R}╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║   ✅ SCAN COMPLETED SUCCESSFULLY                            ║
    ║                                                              ║
    ║   📊 Total Alive Hosts: {len(alive_hosts):<36}║
    ║   📹 CCTV/DVR Devices: {len(cctv_devices):<37}║
    ║   🌐 Network: {network_range:<46}║
    ║   💾 Report: SHOWN ON SCREEN (NO FILE SAVED)                ║
    ║                                                              ║
    ║   Tool: CYBER.IR | Created By: BAIDAR                      ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝{D}
    """)
    print(f"{R}Thank you for using CYBER.IR!{D}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{R}[-] Scan interrupted by user. Exiting...{D}")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n{R}[-] Error: {e}{D}")
        sys.exit(1)

