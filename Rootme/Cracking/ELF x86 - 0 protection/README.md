# Source

[Link](./ch1.bin)

# Solve

- Checksec
```bash
$ checksec ch1.bin 
[*] '/home/Security/CTF/Rootme/Cracking/ELF x86 - 0 protection/ch1.bin'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
```

- GDB Debug

```bash
gdb-peda$ info func
All defined functions:

Non-debugging symbols:
0x08048410  _init
0x08048438  __errno_location@plt
0x08048448  strerror@plt
0x08048458  getchar@plt
0x08048468  __gmon_start__@plt
0x08048478  realloc@plt
0x08048488  __libc_start_main@plt
0x08048498  printf@plt
0x080484a8  fprintf@plt
0x080484b8  malloc@plt
0x080484c8  puts@plt
0x080484d8  strcmp@plt
0x080484f0  _start
0x080485c4  printError
0x080485fe  getString
0x0804869d  main
0x08048740  __libc_csu_fini
0x08048750  __libc_csu_init
0x080487b7  __i686.get_pc_thunk.bx
0x080487ec  _fini
gdb-peda$ disas main
quit
Dump of assembler code for function main:
   0x0804869d <+0>:     lea    ecx,[esp+0x4]
   0x080486a1 <+4>:     and    esp,0xfffffff0
   0x080486a4 <+7>:     push   DWORD PTR [ecx-0x4]
   0x080486a7 <+10>:    push   ebp
   0x080486a8 <+11>:    mov    ebp,esp
   0x080486aa <+13>:    push   ecx
   0x080486ab <+14>:    sub    esp,0x24
   0x080486ae <+17>:    mov    DWORD PTR [ebp-0x8],0x8048841
   0x080486b5 <+24>:    mov    DWORD PTR [esp],0x804884c
   0x080486bc <+31>:    call   0x80484c8 <puts@plt>
   0x080486c1 <+36>:    mov    DWORD PTR [esp],0x804888c
   0x080486c8 <+43>:    call   0x80484c8 <puts@plt>
   0x080486cd <+48>:    mov    DWORD PTR [esp],0x80488cc
   0x080486d4 <+55>:    call   0x80484c8 <puts@plt>
   0x080486d9 <+60>:    mov    DWORD PTR [esp],0x804890c
   0x080486e0 <+67>:    call   0x8048498 <printf@plt>
   0x080486e5 <+72>:    mov    eax,DWORD PTR [ebp-0xc]
   0x080486e8 <+75>:    mov    DWORD PTR [esp],eax
   0x080486eb <+78>:    call   0x80485fe <getString>
   0x080486f0 <+83>:    mov    DWORD PTR [ebp-0xc],eax
   0x080486f3 <+86>:    mov    eax,DWORD PTR [ebp-0x8]
   0x080486f6 <+89>:    mov    DWORD PTR [esp+0x4],eax
   0x080486fa <+93>:    mov    eax,DWORD PTR [ebp-0xc]
   0x080486fd <+96>:    mov    DWORD PTR [esp],eax
   0x08048700 <+99>:    call   0x80484d8 <strcmp@plt>
   0x08048705 <+104>:   test   eax,eax
   0x08048707 <+106>:   jne    0x804871e <main+129>
   0x08048709 <+108>:   mov    eax,DWORD PTR [ebp-0x8]
   0x0804870c <+111>:   mov    DWORD PTR [esp+0x4],eax
   0x08048710 <+115>:   mov    DWORD PTR [esp],0x8048930
   0x08048717 <+122>:   call   0x8048498 <printf@plt>
   0x0804871c <+127>:   jmp    0x804872a <main+141>
   0x0804871e <+129>:   mov    DWORD PTR [esp],0x8048970
   0x08048725 <+136>:   call   0x80484c8 <puts@plt>
   0x0804872a <+141>:   mov    eax,0x0
   0x0804872f <+146>:   add    esp,0x24
   0x08048732 <+149>:   pop    ecx
   0x08048733 <+150>:   pop    ebp
   0x08048734 <+151>:   lea    esp,[ecx-0x4]
   0x08048737 <+154>:   ret
End of assembler dump.
```
- set a breakpoint at address __0x08048700__, just before the __strcmp__ function is called. Then run program and enter the value "aaaaaaaaa".

```bash
gdb-peda$ b *0x08048700

Breakpoint 1 at 0x8048700
gdb-peda$ r

Starting program: /home/Security/CTF/Rootme/Cracking/ELF x86 - 0 protection/ch1.bin
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
############################################################
##        Bienvennue dans ce challenge de cracking        ##
############################################################

Veuillez entrer le mot de passe : aaaaaaaaaaaaaaa
Warning: 'set logging off', an alias for the command 'set logging enabled', is deprecated.
Use 'set logging enabled off'.

Warning: 'set logging on', an alias for the command 'set logging enabled', is deprecated.
Use 'set logging enabled on'.
[----------------------------------registers-----------------------------------]
EAX: 0x804b9d0 ('a' <repeats 15 times>)
EBX: 0xf7fabff4 --> 0x21dd8c
ECX: 0x20 (' ')
EDX: 0x804b5d0 --> 0x0
ESI: 0x8048750 (<__libc_csu_init>:      push   ebp)
EDI: 0xf7ffcba0 --> 0x0
EBP: 0xffffce58 --> 0x0
ESP: 0xffffce30 --> 0x804b9d0 ('a' <repeats 15 times>)
EIP: 0x8048700 (<main+99>:      call   0x80484d8 <strcmp@plt>)
EFLAGS: 0x286 (carry PARITY adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x80486f6 <main+89>: mov    DWORD PTR [esp+0x4],eax
   0x80486fa <main+93>: mov    eax,DWORD PTR [ebp-0xc]
   0x80486fd <main+96>: mov    DWORD PTR [esp],eax
=> 0x8048700 <main+99>: call   0x80484d8 <strcmp@plt>
   0x8048705 <main+104>:        test   eax,eax
   0x8048707 <main+106>:        jne    0x804871e <main+129>
   0x8048709 <main+108>:        mov    eax,DWORD PTR [ebp-0x8]
   0x804870c <main+111>:        mov    DWORD PTR [esp+0x4],eax
Guessed arguments:
arg[0]: 0x804b9d0 ('a' <repeats 15 times>)
arg[1]: 0x8048841 ("123456789")
[------------------------------------stack-------------------------------------]
0000| 0xffffce30 --> 0x804b9d0 ('a' <repeats 15 times>)
0004| 0xffffce34 --> 0x8048841 ("123456789")
0008| 0xffffce38 --> 0x13
0012| 0xffffce3c --> 0xf7fc2400 --> 0xf7d8e000 --> 0x464c457f
0016| 0xffffce40 --> 0xf7daf6ac --> 0x21e04c
0020| 0xffffce44 --> 0xf7fd9d41 (mov    DWORD PTR [esp+0x28],eax)
0024| 0xffffce48 --> 0xf7daa9a2 ("_dl_audit_preinit")
0028| 0xffffce4c --> 0x804b9d0 ('a' <repeats 15 times>)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x08048700 in main ()

gdb-peda$
```

=> We can see two arguments passed to the instruction.
```bash
arg[0]: 0x804b9d0 ('a' <repeats 15 times>)
arg[1]: 0x8048841 ("123456789")
```
S0, the value we need pass in program is __123456789__.

Run program, and pass it on. Then we can get a flag. (It is also 123456789)

```bash
$ ./ch1.bin 
############################################################
##        Bienvennue dans ce challenge de cracking        ##
############################################################

Veuillez entrer le mot de passe : 123456789
Bien joue, vous pouvez valider l'epreuve avec le pass : 123456789!
```

Flag: __123456789__
