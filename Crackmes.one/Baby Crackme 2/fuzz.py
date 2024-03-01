secret_str = "Nkrru&Ngiqkxy"

for i in range(26):
    msg = ""
    for e in secret_str:
        msg += chr(ord(e) - i)
    print(f"{i}: {msg}")
    
# KEY: 6: Hello Hackers