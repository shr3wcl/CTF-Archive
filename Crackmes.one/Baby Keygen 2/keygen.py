import random

def keygen():
    key = "t"
    for i in range(3):
        key += chr(random.randint(33, 127))
    key += '-'
    for i in range(random.randint(0, 5)):
        key += chr(random.randint(33, 127))
        
    return key

print("[+] Key: " + keygen())