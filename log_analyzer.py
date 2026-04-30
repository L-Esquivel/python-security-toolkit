import re
from collections import Counter

def analyze_log(file_path):
    """
    Parses a log file to identify potential brute force attacks.
    It looks for 'Failed password' entries and counts occurrences per IP.
    """
    # Standard regex pattern for failed login attempts in Linux systems
    failed_login_pattern = r"Failed password for .* from ([\d\.]+) port"
    failed_ips = []

    try:
        with open(file_path, "r") as f:
            for line in f:
                match = re.search(failed_login_pattern, line)
                if match:
                    # Append the IP address found in the match
                    failed_ips.append(match.group(1))
        
        # Analyze results
        ip_counts = Counter(failed_ips)
        
        print("\n--- Security Log Analysis Report ---")
        if not failed_ips:
            print("[INFO] No suspicious login attempts detected.")
        else:
            for ip, count in ip_counts.items():
                if count > 3:
                    print(f"[🚨 ALERT] IP {ip}: {count} failed attempts. Possible Brute Force.")
                else:
                    print(f"[i] IP {ip}: {count} failed attempts.")
                    
    except FileNotFoundError:
        print("[!] Error: The specified log file was not found.")

if __name__ == "__main__":
    # Ensure the path points to your samples folder
    analyze_log("samples/server_access.log")
