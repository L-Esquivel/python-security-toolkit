# Python Security Toolkit

**Automated Security Auditing and File Integrity Monitoring Tools in Python**

Set of Python scripts designed to perform security audits, monitor file integrity, and detect potential unauthorized changes in critical systems.

### 🎯 Objective
Provide practical automation for daily security operations, enabling proactive threat detection and system integrity verification without relying solely on heavy commercial tools.

### ✨ Key Features
- File Integrity Monitoring (FIM) with hashing (SHA-256)
- Automated security scanning and baseline comparison
- Log analysis for suspicious activities
- Scheduled monitoring capabilities
- Alert generation and reporting
- Easy-to-extend modular structure

### 🛠️ Technologies
- Python 3.10+
- hashlib (SHA-256)
- os, sys, and datetime modules
- JSON / CSV for baselines and reports
- (Optional) smtplib for email alerts

### 🚀 How to Use

```bash
# Clone the repository
git clone https://github.com/L-Esquivel/python-security-toolkit.git
cd python-security-toolkit

# Create baseline
python3 create_baseline.py

# Run integrity check
python3 integrity_check.py

# Run full security audit
python3 security_audit.py --report

---
This repository is part of a specialized portfolio in IT Operations and Cybersecurity, demonstrating the ability to build custom security tooling*.
