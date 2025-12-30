import subprocess
import argparse
try:
    parser = argparse.ArgumentParser()
    parser.add_argument("host_arg",help="give the host ")
    parser.add_argument("port_arg",help="give the port ")
    args=parser.parse_args()

    try:
        # netcat part 
        port = args.port_arg
        host = args.host_arg
        output = []
        flag = ""
        command = ["nc", host, port]
        res = subprocess.run(
            command,
            capture_output=True,
            timeout=10,
            text=True
        ) 
        for line in res.stdout.strip().splitlines():
            line = line.strip()
            if line.isdigit():          
                output.append(int(line))

        for flag_part in output:
            flag = flag + chr(flag_part)
            
        print("This is the Flag :", flag)
    except Exception as e:
        print("Error in the opening of the nc session !!")
        print("Details:", e)
except:
    print("usage : python3 script_name.py <host> <port>")
