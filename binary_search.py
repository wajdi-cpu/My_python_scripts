import argparse
import subprocess

def main():
    try:
        parser = argparse.ArgumentParser(
            add_help=True,
        )
        parser.add_argument("--user", "-u", required=True, help="user to login with")
        parser.add_argument("--host", "-H", required=True, help="host to connect to")
        parser.add_argument("--port", "-p", required=True, type=int, help="port used in ssh")
        parser.add_argument("--password", help="password (optional)") 
        args = parser.parse_args()
        command = f'ssh {args.user}@{args.host} -p {args.port}'
        nc_session = subprocess.run(
            command,
            shell=True,              
            capture_output=True,
            timeout=10,
            text=True
        )
        print(command)
    except Exception :
        print("Usage : python3 script_name.py -u <user> -H <host> -p <port> --password (optional)")

main()