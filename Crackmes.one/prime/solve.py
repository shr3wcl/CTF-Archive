Str = "Th4t's a P455W0rD"
Str2 = "113e5c6eac71358d3a4727639f55f02457565ae57662a2a2727610d84646"

str3 = []

for i in range(0, len(Str2), 2):
    str3.append(int("0x" + Str2[i:i+2], 16))

primeArr = []

for i in range(30):
    c = str3[i] ^ ord(Str[i % 17])
    primeArr.append(c)

password = ""
    
for i in primeArr:
    v5 = 1
    for j in range(0x100):
        v5 = v5 * 0x81 % 0xFB
        if v5 == i:
            password += chr(j+1)
            break

print(password)
        