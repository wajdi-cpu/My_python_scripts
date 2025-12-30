import subprocess

try:
    # netcat part 
    port = "49419"
    host = "wily-courier.picoctf.net"
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