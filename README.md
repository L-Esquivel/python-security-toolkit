# Python Security Toolkit 🛡️

A collection of utility scripts for cybersecurity tasks.

## 1. File Integrity Monitor (`file_integrity_checker.py`)
This tool allows users to verify if a file has been tampered with by comparing its current SHA-256 hash against a known baseline.

### How it works:
1. It reads the file in binary mode.
2. It generates a unique 64-character signature (Hash).
3. If even a single character in the file changes, the hash changes completely (**Avalanche Effect**).

### Usage:
`python3 file_integrity_checker.py`

### 2. Security Log Analyzer (`log_analyzer.py`)
Automated script to parse server logs and identify potential brute-force attacks.
- **How it works:** It uses Regular Expressions (Regex) to scan for "Failed password" patterns and flags any IP address with more than 3 failed attempts.
- **Key Skills:** Regex, Data Parsing, Incident Identification.
