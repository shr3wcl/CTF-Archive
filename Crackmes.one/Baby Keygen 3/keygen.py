import random

def keygen():
    key = 'A'
    for i in range(10):
        if i == 2 or i == 6:
            key += '-'
        else:
            key += chr(random.randint(33, 127))
    
    print("[!] Length: " + str(len(key)))
    print("[!] Element at index 0: " + key[0])
    print("[!] Element at index 3: " + key[3])
    print("[!] Element at index 7: " + key[7])
    print("[+] Key: " + key)
    
keygen()

# Password: nanyKeygen