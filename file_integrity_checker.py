import hashlib
import os

def calculate_sha256(file_path):
    """Calculates the SHA-256 hash of a given file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            # Read the file in chunks to handle large files
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def monitor_file(file_to_check, original_hash):
    """Compares the current hash with the original one."""
    current_hash = calculate_sha256(file_to_check)
    
    if current_hash is None:
        print(f"[!] Error: File '{file_to_check}' not found.")
    elif current_hash == original_hash:
        print(f"[✅] Integrity Verified: No changes detected in '{file_to_check}'.")
    else:
        print(f"[🚨] ALERT: File '{file_to_check}' has been MODIFIED!")
        print(f"Original Hash: {original_hash}")
        print(f"Current Hash:  {current_hash}")

# --- Example of usage ---
if __name__ == "__main__":
    # First, we define a file to protect
    target = "important_config.txt"
    
    # Create the file if it doesn't exist for testing
    if not os.path.exists(target):
        with open(target, "w") as f:
            f.write("System Configuration: Version 1.0")

    # Generate the baseline hash
    baseline = calculate_sha256(target)
    print(f"[*] Baseline established for {target}: {baseline}")

    # Verify integrity
    monitor_file(target, baseline)