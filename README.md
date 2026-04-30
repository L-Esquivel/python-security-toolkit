# Python Security Toolkit 🛡️

A collection of practical Python scripts developed for security automation, log analysis, and network reconnaissance. This toolkit demonstrates my ability to apply programming to real-world cybersecurity challenges.

## 🚀 Tools Included

### 1. File Integrity Monitor (`file_integrity_checker.py`)
Verifies the integrity of sensitive files by comparing their current SHA-256 hash against a baseline.
- **Key Skills:** Cryptography (Hashing), File I/O, Integrity Monitoring.
- **Use Case:** Detecting unauthorized changes in system configuration files.

### 2. Security Log Analyzer (`log_analyzer.py`)
Parses server logs to identify potential security threats, such as brute-force attacks.
- **Key Skills:** Regular Expressions (Regex), Data Parsing, Incident Identification.
- **Use Case:** Monitoring `auth.log` or `access.log` to flag IPs with multiple failed login attempts.

### 3. Basic Port Scanner (`port_scanner.py`)
A reconnaissance tool that scans a target IP for open ports using TCP connections.
- **Key Skills:** Networking Protocols (TCP/IP), Socket Programming, Footprinting.
- **Use Case:** Identifying exposed services on a network host.

---

## 📁 Repository Structure
- `/samples`: Contains `server_access.log`, a simulated log file used to test the **Log Analyzer**.
- `file_integrity_checker.py`: Main script for hash verification.
- `log_analyzer.py`: Main script for log auditing.
- `port_scanner.py`: Main script for network scanning.

## 🛠️ Getting Started
1. Clone the repository:
   ```bash
   git clone [https://github.com/L-Esquivel/python-security-toolkit.git](https://github.com/L-Esquivel/python-security-toolkit.git)
