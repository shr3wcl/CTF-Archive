from pwn import *

exe = remote("94.237.49.11", 56864)
exe.recvuntil(b">>")
exe.send(b"64-bit")

exe.interactive()