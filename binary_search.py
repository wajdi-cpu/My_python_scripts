#!/usr/bin/env python3
import sys
import pexpect
import argparse

def binary_search(child):
    low, high = 1, 1000
    solved = False

    for attempt in range(10):
        guess = (low + high) // 2
        print(f"[{attempt+1}/10] Guessing: {guess}")
        child.sendline(str(guess))

        i = child.expect([
            "Higher!",
            "Lower!",
            "Congratulations!",
            "Please enter a valid number."
        ])

        if i == 0:
            low = guess + 1
        elif i == 1:
            high = guess - 1
        elif i == 2:
            child.expect("Here's your flag:", timeout=5)
            flag = child.readline().strip()
            print(f"\n FLAG: {flag}")
            solved = True
            break

    if not solved:
        print("[-] Failed to solve.")

def main():
    parser = argparse.ArgumentParser(description="Automate SSH guessing game using binary search.")
    parser.add_argument("--user", "-u", required=True, help="SSH username")
    parser.add_argument("--host", "-H", required=True, help="SSH host")
    parser.add_argument("--port", "-p", required=True, type=int, help="SSH port")
    parser.add_argument("--password", required=True, help="SSH password")
    
    args = parser.parse_args()

    command = f"ssh {args.user}@{args.host} -p {args.port}"
    print(f"[+] Starting SSH session: {command}")

    child = pexpect.spawn(command, encoding='utf-8', timeout=20)

    try:
        index = child.expect([".*Are you sure you want to continue connecting.*", ".*[Pp]assword:"], timeout=5)
        if index == 0:
            child.sendline("yes")
    except pexpect.TIMEOUT:
        pass

    try:
        child.expect(".*[Pp]assword:", timeout=10)
        child.sendline(args.password)
    except pexpect.TIMEOUT:
        print("[-] Timed out waiting for password prompt.")
        print("Output so far:", child.before)
        sys.exit(1)

    try:
        child.expect("I'm thinking of a number between 1 and 1000.", timeout=10)
        print("[+] Game started!")
    except pexpect.TIMEOUT:
        print("[-] Did not see game start message.")
        print("Output so far:", child.before)
        sys.exit(1)

    binary_search(child)
    child.close()

if __name__ == "__main__":
    main()
