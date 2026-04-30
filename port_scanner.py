import socket

def scan_ports(target_ip, port_range):
    print(f"--- Scanning Target: {target_ip} ---")
    open_ports = []

    for port in port_range:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a short timeout for faster scanning
        s.settimeout(0.5)
        
        # Attempt to connect to the port
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"[🔓] Port {port}: OPEN")
            open_ports.append(port)
        s.close()
    
    print("--- Scan Finished ---")
    if not open_ports:
        print("No open ports found in the selected range.")
    else:
        print(f"Total open ports found: {len(open_ports)}")

if __name__ == "__main__":
    target = "127.0.0.1" 
    # Scanning common ports: SSH, HTTP, HTTPS, MySQL
    common_ports = [22, 80, 443, 3306, 8080]
    
    scan_ports(target, common_ports)
