# Source

Papa brought me a packed present! let's open it.

Download : http://pwnable.kr/bin/flag

This is reversing task. all you need is binary

# 🚩Solve

```bash
$ checksec flag
[*] '/home/Security/pwnableKR/flag/flag'
    Arch:     amd64-64-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX unknown - GNU_STACK missing
    PIE:      No PIE (0x400000)
    Stack:    Executable
    RWX:      Has RWX segments
    Packer:   Packed with UPX
```

This binary file has been packed by UPX. So, we should be unpack it first.
Use UPX tool with this command:

```bash
sudo apt update && sudo apt upgrade
sudo apt-get install upx
$ upx -d flag
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2020
UPX 3.96        Markus Oberhumer, Laszlo Molnar & John Reiser   Jan 23rd 2020

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
    883745 <-    335288   37.94%   linux/amd64   flag

Unpacked 1 file.
```

Checksec it again. So it has been unpacked.

```bash
$ checksec flag 
[*] '/home/Security/pwnableKR/flag/flag'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

Next, disassemble it to view the source code:

```bash
$ gdb -q flag
Reading symbols from flag...
(No debugging symbols found in flag)
gdb-peda$ disas main
Dump of assembler code for function main:
   0x0000000000401164 <+0>:     push   rbp
   0x0000000000401165 <+1>:     mov    rbp,rsp
   0x0000000000401168 <+4>:     sub    rsp,0x10
   0x000000000040116c <+8>:     mov    edi,0x496658
   0x0000000000401171 <+13>:    call   0x402080 <puts>
   0x0000000000401176 <+18>:    mov    edi,0x64
   0x000000000040117b <+23>:    call   0x4099d0 <malloc>
   0x0000000000401180 <+28>:    mov    QWORD PTR [rbp-0x8],rax
   0x0000000000401184 <+32>:    mov    rdx,QWORD PTR [rip+0x2c0ee5]        # 0x6c2070 <flag>
   0x000000000040118b <+39>:    mov    rax,QWORD PTR [rbp-0x8]
   0x000000000040118f <+43>:    mov    rsi,rdx
   0x0000000000401192 <+46>:    mov    rdi,rax
   0x0000000000401195 <+49>:    call   0x400320
   0x000000000040119a <+54>:    mov    eax,0x0
   0x000000000040119f <+59>:    leave
   0x00000000004011a0 <+60>:    ret
End of assembler dump.
```

Set breakpoint at __0x000000000040118b__, right after the flag is passed to __rdx__ and print its value and we have the flag:

```bash
gdb-peda$ b *0x000000000040118b
Breakpoint 1 at 0x40118b
gdb-peda$ r
Starting program: /home/Security/pwnableKR/flag/flag
I will malloc() and strcpy the flag there. take it.
Warning: 'set logging off', an alias for the command 'set logging enabled', is deprecated.
Use 'set logging enabled off'.

Warning: 'set logging on', an alias for the command 'set logging enabled', is deprecated.
Use 'set logging enabled on'.

Breakpoint 1, 0x000000000040118b in main ()

gdb-peda$ x/s $rdx
0x496628:       "UPX...? sounds like a delivery service :)"
gdb-peda$
```

So flag is: ___UPX...? sounds like a delivery service :\)___