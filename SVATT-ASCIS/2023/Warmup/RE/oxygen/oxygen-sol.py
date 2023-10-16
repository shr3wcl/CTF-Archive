string = b'n[}>}C]qRm['
result = ''
for x in range(len(string)):
    for eax in range(256):
        if x%2==0:
            if (eax | 0x0A) - (eax& 0x0A) == string[x]:
                result += chr(eax)
        else:
            if(eax|0x0A)+(eax&0x0A) == string[x]:
                result += chr(eax)
print(result)