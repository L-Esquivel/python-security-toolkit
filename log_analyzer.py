import re
from collections import Counter

def analyze_log(file_path):
    # Pattern to find "Failed password" errors (standard in Linux servers)
    failed_login_pattern = r"Failed password for .* from ([\d\.]+) port"
    
    failed_ips = []

    try:
        with open(file_path, "r") as f:
            for line in f:
                match = re.search(failed_login_pattern, line)
                if match:
                    # Extract the IP address that attempted the login
                    failed_ips.append(match.group(1))
        
        # Count occurrences for each IP
        counts = Counter(failed_ips)
        
        print("--- Security Log Analysis Report ---")
        if not failed_ips:
            print("[✅] No suspicious failed logins detected.")
        else:
            print("[🚨] Suspicious activity detected!")
            for ip, count in counts.items():
                if count > 3: # Flag as alert if more than 3 failures
                    print(f"ALERT: IP {ip} failed login {count} times (Potential Brute Force)")
                else:
                    print(f"Info: IP {ip} failed login {count} times")
                    
    except FileNotFoundError:
        print("[!] Error: Log file not found.")

if __name__ == "__main__":
    # Pointing to the samples directory
    analyze_log("samples/server_access.log")
