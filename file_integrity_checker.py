import hashlib

def get_file_hash(file_path):
    """
    Generates a SHA-256 hash for a given file to monitor unauthorized changes.
    """
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            # Read file in 4KB chunks for memory efficiency
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"[!] Error: File '{file_path}' not found.")
        return None

if __name__ == "__main__":
    # Example usage: Replace with a real file path to test
    test_file = "samples/server_access.log"
    file_hash = get_file_hash(test_file)
    
    if file_hash:
        print(f"\n--- Integrity Report ---")
        print(f"File: {test_file}")
        print(f"SHA-256 Hash: {file_hash}")
