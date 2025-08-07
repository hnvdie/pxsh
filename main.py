
import os
import sys
import argparse
import subprocess

# Kosong untuk publikasi
hostConfig = []

# Simple ANSI color
GREEN = "\033[92m"
RESET = "\033[0m"

def banner():
    os.system("clear")
    print(r"""       _,    _   _    ,_
  .o888P     Y8o8Y     Y888o.
 d88888      88888      88888b
d888888b_  _d88888b_  _d888888b
8888888888888888888888888888888  PXSH - Parallel x SSH
8888888888888888888888888888888  Batch command runner over SSH
YJGS8P"Y888P"Y888P"Y888P"Y8888P
 Y888   '8'   Y8P   '8'   888Y
  '8o          V          o8'
    `                     `
""")

def send(command, host):
    try:
        subprocess.run(["ssh", host, command])
    except Exception as e:
        print(f"[!] Failed to send command to {host}: {e}")

def check_active(host):
    try:
        result = subprocess.run(
            ["ping", "-c", "1", "-W", "1", host.split('@')[-1]],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    except:
        return False

def main():
    parser = argparse.ArgumentParser(
        description="🔐 Pxsh — Execute or ping multiple remote servers via SSH."
    )
    parser.add_argument(
        "--server",
        help="List of target SSH servers separated by commas (e.g. user@host1,user@host2). "
             "If omitted, will use internal hostConfig list."
    )
    parser.add_argument(
        "--send",
        help="Shell command to send to each server. You can use piping, semicolons, etc."
    )
    parser.add_argument(
        "--active",
        action="store_true",
        help="Check if the target server(s) are reachable via ping (returns 'Active' or 'Inactive')."
    )
    args = parser.parse_args()

    if args.server:
        hostnames = args.server.split(",")
    else:
        hostnames = hostConfig

    if args.send:
        for host in hostnames:
            print(f"[+] Sending command to {host}")
            send(args.send, host)

    elif args.active:
        for host in hostnames:
            status = check_active(host)
            status_str = f"{GREEN}Active{RESET}" if status else "Inactive"
            print(f"[+] {host} status: {status_str}")

if __name__ == "__main__":
    banner()
    main()
Commander
