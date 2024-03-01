encrypt_msg = "\x22\x33\x20\x22\x2A\x2C\x24"

for i in range(1000):
    msg = ""
    for e in encrypt_msg:
        msg += chr(ord(e) ^ i)
    print(f"{i}: {msg}")
    
# KEY: 65:crackme 97:CRACKME