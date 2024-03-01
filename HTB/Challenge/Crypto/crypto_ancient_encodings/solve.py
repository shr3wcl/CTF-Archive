import base64

f = open('./output.txt','r')
ct = bytes.fromhex(f.read().split('0x')[1])
f.close()
flag = base64.b64decode(ct)
print(flag)
