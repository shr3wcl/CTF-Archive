import random

def keygen():
    key = 'A'
    for i in range(10):
        if i == 2 or i == 6:
            key += 'X'
        else:
            key += chr(random.randint(33, 127))
            
    return key
    
print("[+] Key 1: " + keygen())
print("[+] Key 2: " + keygen())
print("[+] Key 3: " + keygen())

# Password: nanyJeygen