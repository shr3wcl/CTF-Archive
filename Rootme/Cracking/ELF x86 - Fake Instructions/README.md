# Source

[Link](./crackme)

# Solve

1. File analysis:
```bash
$ checksec crackme 
[*] '/home/Security/CTF/Rootme/Cracking/ELF x86 - Fake Instructions/crackme'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
```

2. Disassembled using IDA 32bit and GDB-peda:

- In IDA:

    - __Main__ func:
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  const char **v4; // [esp+10h] [ebp-9Ch]
  _BYTE *dest; // [esp+18h] [ebp-94h]
  char v6[100]; // [esp+1Eh] [ebp-8Eh] BYREF
  char v7[30]; // [esp+82h] [ebp-2Ah] BYREF
  unsigned int v8; // [esp+A0h] [ebp-Ch]
  int *p_argc; // [esp+A4h] [ebp-8h]

  p_argc = &argc;
  v4 = argv;
  v8 = __readgsdword(0x14u);
  if ( argc != 2 )
  {
    printf("(*) -Syntaxe: %s [password] \n", *argv);
    exit(0);
  }
  dest = malloc(0x1Du);
  memcpy(dest, &unk_8048910, 0x1Fu);
  memset(v6, 0, sizeof(v6));
  memcpy(v6, "_Celebration", 0xDu);
  dest[5] = 99;
  dest[22] = 0;
  function_ptr_2175 = (int (__cdecl *)(_DWORD, _DWORD))WPA;
  strcpy(v7, v4[1]);
  dest[8] = 95;
  dest[9] = 46;
  return function_ptr_2175(v7, dest);
}
```
 Here the first password is copied into variable __v7__ and then passed to the __WPA__ function along with __dest__.

- In __WPA__ func:

```c
void __cdecl __noreturn WPA(char *s1, char *s2)
{
  int v2; // [esp+0h] [ebp-8h]
  int v3; // [esp+4h] [ebp-4h]
  int savedregs; // [esp+8h] [ebp+0h]

  s2[11] = 13;
  s2[12] = 10;
  puts(s);
  if ( !strcmp(s1, s2) )
    blowfish(v2, v3, savedregs);
  RS4();
}
```
- In this function, the value of __dest__ is changed in some elements. It is then compared with the transmitted __password__. If it is correct, call the __blowfish__ function, otherwise call the __RS4__ function.
- In RS4:
```c
void __noreturn RS4()
{
  printf("le voie de la sagesse te guidera, tache de trouver le mot de passe petit padawaan \n ");
  exit(0);
}
```
- This function simply prints a message if the password is incorrect
- In __blowfist__ func:
```c
void __noreturn blowfish()
{
  unsigned int i; // [esp+Ch] [ebp-4Ch]
  _BYTE *v1; // [esp+14h] [ebp-44h]
  _BYTE v2[60]; // [esp+18h] [ebp-40h] BYREF
  unsigned int v3; // [esp+54h] [ebp-4h]

  v3 = __readgsdword(0x14u);
  *(_DWORD *)v2 = 1700948332;
  *(_DWORD *)&v2[4] = -1446808462;
  *(_DWORD *)&v2[8] = 33;
  for ( i = 0; i < 0x14; i += 4 )
    *(_DWORD *)&v2[i + 12] = 0;
  v1 = &v2[i + 12];
  *(_WORD *)v1 = 0;
  v1[2] = 0;
  *(_DWORD *)&v2[35] = 1197682783;
  *(_DWORD *)&v2[39] = 1832215402;
  *(_DWORD *)&v2[43] = 1412771423;
  *(_DWORD *)&v2[47] = 948421427;
  *(_DWORD *)&v2[51] = -1020245437;
  *(_DWORD *)&v2[55] = 961034624;
  v2[59] = 0;
  printf(aAuthentificati, v2);
  exit(0);
}
// aAuthentificati = "+) Authentification r"
```
- Analyzing this function, this function will initialize a value string and then print it with a message when the password is passed correctly.
*** 
- GDB:
- I use gdb and set a breakpoint at the address where the comparison is done (__0x804847c__). I set the value of the __$eax__ register to 0x0 so that the comparison function looks correct and jumps into executing the __blowfish__ function.

```bash
$ gdb -q crackme
Reading symbols from crackme...
gdb-peda$ disas WPA
Dump of assembler code for function WPA:
   0x080486c4 <+0>:     push   ebp
   0x080486c5 <+1>:     mov    ebp,esp
   0x080486c7 <+3>:     sub    esp,0x8
   0x080486ca <+6>:     mov    eax,DWORD PTR [ebp+0xc]
   0x080486cd <+9>:     add    eax,0xb
   0x080486d0 <+12>:    mov    BYTE PTR [eax],0xd
   0x080486d3 <+15>:    mov    eax,DWORD PTR [ebp+0xc]
   0x080486d6 <+18>:    add    eax,0xc
   0x080486d9 <+21>:    mov    BYTE PTR [eax],0xa
   0x080486dc <+24>:    mov    DWORD PTR [esp],0x804893c
   0x080486e3 <+31>:    call   0x804846c <puts@plt>
   0x080486e8 <+36>:    mov    eax,DWORD PTR [ebp+0xc]
   0x080486eb <+39>:    mov    DWORD PTR [esp+0x4],eax
   0x080486ef <+43>:    mov    eax,DWORD PTR [ebp+0x8]
   0x080486f2 <+46>:    mov    DWORD PTR [esp],eax
   0x080486f5 <+49>:    call   0x804847c <strcmp@plt>
   0x080486fa <+54>:    test   eax,eax
   0x080486fc <+56>:    jne    0x804870f <WPA+75>
   0x080486fe <+58>:    call   0x804872c <blowfish>
   0x08048703 <+63>:    mov    DWORD PTR [esp],0x0
   0x0804870a <+70>:    call   0x804848c <exit@plt>
   0x0804870f <+75>:    call   0x8048803 <RS4>
   0x08048714 <+80>:    mov    DWORD PTR [esp],0x8048964
   0x0804871b <+87>:    call   0x804846c <puts@plt>
   0x08048720 <+92>:    mov    DWORD PTR [esp],0x1
   0x08048727 <+99>:    call   0x804848c <exit@plt>
End of assembler dump.
gdb-peda$ b *0x080486f5
Breakpoint 1 at 0x80486f5
gdb-peda$ run aaaaaaaaaaaa
Starting program: /mnt/c/Users/Minh Tri/Documents/Security/CTF/Rootme/Cracking/ELF x86 - Fake Instructions/crackme aaaaaaaaaaaa
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Vérification de votre mot de passe..
Warning: 'set logging off', an alias for the command 'set logging enabled', is deprecated.
Use 'set logging enabled off'.

Warning: 'set logging on', an alias for the command 'set logging enabled', is deprecated.
Use 'set logging enabled on'.
[----------------------------------registers-----------------------------------]
EAX: 0xffffce0e ('a' <repeats 12 times>)
EBX: 0xf7fabff4 --> 0x21dd8c
ECX: 0xf7fad9b8 --> 0x0
EDX: 0x0
ESI: 0x8048840 (<__libc_csu_init>:      push   ebp)
EDI: 0xffffce0e ('a' <repeats 12 times>)
EBP: 0xffffcd78 --> 0xffffce38 --> 0x0
ESP: 0xffffcd70 --> 0xffffce0e ('a' <repeats 12 times>)
EIP: 0x80486f5 (<WPA+49>:       call   0x804847c <strcmp@plt>)
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x80486eb <WPA+39>:  mov    DWORD PTR [esp+0x4],eax
   0x80486ef <WPA+43>:  mov    eax,DWORD PTR [ebp+0x8]
   0x80486f2 <WPA+46>:  mov    DWORD PTR [esp],eax
=> 0x80486f5 <WPA+49>:  call   0x804847c <strcmp@plt>
   0x80486fa <WPA+54>:  test   eax,eax
   0x80486fc <WPA+56>:  jne    0x804870f <WPA+75>
   0x80486fe <WPA+58>:  call   0x804872c <blowfish>
   0x8048703 <WPA+63>:  mov    DWORD PTR [esp],0x0
Guessed arguments:
arg[0]: 0xffffce0e ('a' <repeats 12 times>)
arg[1]: 0x804b1a0 ("_0cGjc5m_.5\r\nÇ8CJ0À9")
[------------------------------------stack-------------------------------------]
0000| 0xffffcd70 --> 0xffffce0e ('a' <repeats 12 times>)
0004| 0xffffcd74 --> 0x804b1a0 ("_0cGjc5m_.5\r\nÇ8CJ0À9")
0008| 0xffffcd78 --> 0xffffce38 --> 0x0
0012| 0xffffcd7c --> 0x80486a6 (<main+338>:     mov    edx,DWORD PTR [ebp-0xc])
0016| 0xffffcd80 --> 0xffffce0e ('a' <repeats 12 times>)
0020| 0xffffcd84 --> 0x804b1a0 ("_0cGjc5m_.5\r\nÇ8CJ0À9")
0024| 0xffffcd88 --> 0xd ('\r')
0028| 0xffffcd8c --> 0x19
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x080486f5 in WPA ()
gdb-peda$ n
[----------------------------------registers-----------------------------------]
EAX: 0x1
EBX: 0xf7fabff4 --> 0x21dd8c
ECX: 0x5f ('_')
EDX: 0xffffce0e ('a' <repeats 12 times>)
ESI: 0x8048840 (<__libc_csu_init>:      push   ebp)
EDI: 0xffffce0e ('a' <repeats 12 times>)
EBP: 0xffffcd78 --> 0xffffce38 --> 0x0
ESP: 0xffffcd70 --> 0xffffce0e ('a' <repeats 12 times>)
EIP: 0x80486fa (<WPA+54>:       test   eax,eax)
EFLAGS: 0x212 (carry parity ADJUST zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x80486ef <WPA+43>:  mov    eax,DWORD PTR [ebp+0x8]
   0x80486f2 <WPA+46>:  mov    DWORD PTR [esp],eax
   0x80486f5 <WPA+49>:  call   0x804847c <strcmp@plt>
=> 0x80486fa <WPA+54>:  test   eax,eax
   0x80486fc <WPA+56>:  jne    0x804870f <WPA+75>
   0x80486fe <WPA+58>:  call   0x804872c <blowfish>
   0x8048703 <WPA+63>:  mov    DWORD PTR [esp],0x0
   0x804870a <WPA+70>:  call   0x804848c <exit@plt>
[------------------------------------stack-------------------------------------]
0000| 0xffffcd70 --> 0xffffce0e ('a' <repeats 12 times>)
0004| 0xffffcd74 --> 0x804b1a0 ("_0cGjc5m_.5\r\nÇ8CJ0À9")
0008| 0xffffcd78 --> 0xffffce38 --> 0x0
0012| 0xffffcd7c --> 0x80486a6 (<main+338>:     mov    edx,DWORD PTR [ebp-0xc])
0016| 0xffffcd80 --> 0xffffce0e ('a' <repeats 12 times>)
0020| 0xffffcd84 --> 0x804b1a0 ("_0cGjc5m_.5\r\nÇ8CJ0À9")
0024| 0xffffcd88 --> 0xd ('\r')
0028| 0xffffcd8c --> 0x19
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
0x080486fa in WPA ()
gdb-peda$ p $eax
$1 = 0x1
gdb-peda$ set $eax=0x0
gdb-peda$ n
[----------------------------------registers-----------------------------------]
EAX: 0x0
EBX: 0xf7fabff4 --> 0x21dd8c
ECX: 0x5f ('_')
EDX: 0xffffce0e ('a' <repeats 12 times>)
ESI: 0x8048840 (<__libc_csu_init>:      push   ebp)
EDI: 0xffffce0e ('a' <repeats 12 times>)
EBP: 0xffffcd78 --> 0xffffce38 --> 0x0
ESP: 0xffffcd70 --> 0xffffce0e ('a' <repeats 12 times>)
EIP: 0x80486fc (<WPA+56>:       jne    0x804870f <WPA+75>)
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x80486f2 <WPA+46>:  mov    DWORD PTR [esp],eax
   0x80486f5 <WPA+49>:  call   0x804847c <strcmp@plt>
   0x80486fa <WPA+54>:  test   eax,eax
=> 0x80486fc <WPA+56>:  jne    0x804870f <WPA+75>
   0x80486fe <WPA+58>:  call   0x804872c <blowfish>
   0x8048703 <WPA+63>:  mov    DWORD PTR [esp],0x0
   0x804870a <WPA+70>:  call   0x804848c <exit@plt>
   0x804870f <WPA+75>:  call   0x8048803 <RS4>
                                                              JUMP is NOT taken
[------------------------------------stack-------------------------------------]
0000| 0xffffcd70 --> 0xffffce0e ('a' <repeats 12 times>)
0004| 0xffffcd74 --> 0x804b1a0 ("_0cGjc5m_.5\r\nÇ8CJ0À9")
0008| 0xffffcd78 --> 0xffffce38 --> 0x0
0012| 0xffffcd7c --> 0x80486a6 (<main+338>:     mov    edx,DWORD PTR [ebp-0xc])
0016| 0xffffcd80 --> 0xffffce0e ('a' <repeats 12 times>)
0020| 0xffffcd84 --> 0x804b1a0 ("_0cGjc5m_.5\r\nÇ8CJ0À9")
0024| 0xffffcd88 --> 0xd ('\r')
0028| 0xffffcd8c --> 0x19
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
0x080486fc in WPA ()
gdb-peda$
[----------------------------------registers-----------------------------------]
EAX: 0x0
EBX: 0xf7fabff4 --> 0x21dd8c
ECX: 0x5f ('_')
EDX: 0xffffce0e ('a' <repeats 12 times>)
ESI: 0x8048840 (<__libc_csu_init>:      push   ebp)
EDI: 0xffffce0e ('a' <repeats 12 times>)
EBP: 0xffffcd78 --> 0xffffce38 --> 0x0
ESP: 0xffffcd70 --> 0xffffce0e ('a' <repeats 12 times>)
EIP: 0x80486fe (<WPA+58>:       call   0x804872c <blowfish>)
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x80486f5 <WPA+49>:  call   0x804847c <strcmp@plt>
   0x80486fa <WPA+54>:  test   eax,eax
   0x80486fc <WPA+56>:  jne    0x804870f <WPA+75>
=> 0x80486fe <WPA+58>:  call   0x804872c <blowfish>
   0x8048703 <WPA+63>:  mov    DWORD PTR [esp],0x0
   0x804870a <WPA+70>:  call   0x804848c <exit@plt>
   0x804870f <WPA+75>:  call   0x8048803 <RS4>
   0x8048714 <WPA+80>:  mov    DWORD PTR [esp],0x8048964
No argument
[------------------------------------stack-------------------------------------]
0000| 0xffffcd70 --> 0xffffce0e ('a' <repeats 12 times>)
0004| 0xffffcd74 --> 0x804b1a0 ("_0cGjc5m_.5\r\nÇ8CJ0À9")
0008| 0xffffcd78 --> 0xffffce38 --> 0x0
0012| 0xffffcd7c --> 0x80486a6 (<main+338>:     mov    edx,DWORD PTR [ebp-0xc])
0016| 0xffffcd80 --> 0xffffce0e ('a' <repeats 12 times>)
0020| 0xffffcd84 --> 0x804b1a0 ("_0cGjc5m_.5\r\nÇ8CJ0À9")
0024| 0xffffcd88 --> 0xd ('\r')
0028| 0xffffcd8c --> 0x19
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
0x080486fe in WPA ()
gdb-peda$
'+) Authentification réussie...
 U'r root!

 sh 3.0 # password: liberté!                               <--------------------------- Here is result of blowfish func
[Inferior 1 (process 109) exited normally]
Warning: not running
gdb-peda$
```
-  So the blowfish function will print the password ( `password: liberté! ` ), this is also the flag

## `🚩Flag: liberté!`