import os

# Sample virus signatures (could be patterns from malware)
signatures = [b"malicious_pattern_1", b"malicious_pattern_2"]

def is_infected(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()
        for sig in signatures:
            if sig in content:
                return True
    return False

def scan_directory(directory):
    print(f"\nScanning directory: {directory}")
    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            try:
                if is_infected(full_path):
                    print(f"[INFECTED] {full_path}")
                else:
                    print(f"[CLEAN] {full_path}")
            except Exception as e:
                print(f"[ERROR] Could not read {full_path}: {e}")

def main():
    print("=== Lab 10: Simple Virus Scanner ===")
    directory = input("Enter path to directory to scan: ")
    if os.path.isdir(directory):
        scan_directory(directory)
    else:
        print("[!] Invalid directory path.")

if __name__ == "__main__":
    main()
