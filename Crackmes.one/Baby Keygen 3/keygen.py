import random

def keygen():
    key = 'A'
    for i in range(10):
        if i == 2 or i == 6:
            key += '-'
        else:
            key += chr(random.randint(33, 127))
            
    print("[+] Key: " + key)
    
keygen()

# Password: nanyKeygen