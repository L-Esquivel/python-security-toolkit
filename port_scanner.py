import socket

def scan_ports(target_ip, port_range):
    """
    Attempts to establish TCP connections to a range of ports to check for open services.
    """
    print(f"\n--- Starting Scan on Target: {target_ip} ---")
    open_ports = []

    for port in port_range:
        # Create a TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 0.5 second timeout to keep the scan efficient
        s.settimeout(0.5)
        
        # connect_ex returns 0 for a successful connection
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"[🔓] Port {port}: OPEN")
            open_ports.append(port)
        s.close()
    
    print("\n--- Scan Summary ---")
    if open_ports:
        print(f"Total open ports found: {len(open_ports)}")
    else:
        print("No open ports detected in the provided range.")

if __name__ == "__main__":
    # Localhost for safe testing
    target = "127.0.0.1" 
    # Common ports: SSH, HTTP, HTTPS, MySQL, HTTP-Alt
    common_ports = [22, 80, 443, 3306, 8080]
    
    scan_ports(target, common_ports)
