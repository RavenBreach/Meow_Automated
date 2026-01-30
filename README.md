# Meow_Automated

### What is Meow?

Meow is the first machine in the **Tier 0** of the StartingPoint program on Hack The Box.

**Vulnerability**: Misconfigured Telnet server allowing unauthenticated root access

**Difficulty**: Very Easy

### Prerequisites

To run this exploit script, you need:

1. **Python 3.13+** installed
   ```bash
   python --version
   ```

2. **Telnetlib** - You need to install this because it is not enabled on Python 3.13
   ```bash
   wget https://raw.githubusercontent.com/python/cpython/3.12/Lib/telnetlib.py
   ```

3. **Deactivate security** - You need to deactivate this security that make the script crashes
    ```
    sed -i '/warnings._deprecated/d' telnetlib.py
    ```

### How to Use the Script

#### Two Modes Available

**Shell Mode** - Interactive access
```bash
python meow_automated.py -s <TARGET_IP>
```
You get full shell control. Type commands manually.

**Flag Mode** - Auto extract flag
```bash
python meow_automated.py -f <TARGET_IP>
```
Automatically retrieves and displays the flag.

#### Example

```bash
# Get interactive shell
python meow_automated.py -s 10.129.45.123

# Auto get flag
python meow_automated.py -f 10.129.45.123
```

### How It Works

1. Connects to Telnet (port 23)
2. Waits for "login: " prompt
3. Sends "root" user
4. In shell mode: gives you interactive access
5. In flag mode: runs `cat flag.txt` and shows the flag

### Links
- Find the writeup (French) on [Medium](#https://medium.com/@ravenbreach/comment-craquer-la-machine-la-plus-difficile-de-htb-5c4de7255bcf)
- Find the walkthough (French) on [Youtube](#https://youtu.be/RGixHuuqmsI?si=PPI830kFhjHKkQQW)
