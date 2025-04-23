import hashlib

def detect_collision(limit=100000):
    seen_hashes = {}
    for i in range(limit):
        input_str = str(i)
        hash_val = hashlib.md5(input_str.encode()).hexdigest()

        if hash_val in seen_hashes:
            print(f"[!] Collision found between '{seen_hashes[hash_val]}' and '{input_str}'")
            return
        seen_hashes[hash_val] = input_str

    print("No collision found in the given range.")

def main():
    print("=== Lab 6: MD5 Hash Collision Detection ===")
    detect_collision()

if __name__ == "__main__":
    main()
