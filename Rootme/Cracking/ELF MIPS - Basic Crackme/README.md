# Source

[Link](./ch27.bin)

# Solve
- File analysis:
```bash
$ checksec ch27.bin
[*] '/home/Security/CTF/Rootme/Cracking/ELF MIPS - Basic Crackme/ch27.bin'
    Arch:     mips-32-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x400000)
    RWX:      Has RWX segments
```
- Disassembled using IDA 32bit with `Processor type is MIPS little endian`
- This is source code of main function:
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int i; // [sp+18h] [+18h] BYREF
  char v5[4]; // [sp+1Ch] [+1Ch] BYREF
  char v6; // [sp+20h] [+20h]
  char v7; // [sp+21h] [+21h]
  char v8; // [sp+22h] [+22h]
  char v9; // [sp+23h] [+23h]
  char v10; // [sp+2Dh] [+2Dh]
  char v11; // [sp+2Eh] [+2Eh]
  int v12; // [sp+60h] [+60h]
  int v13; // [sp+64h] [+64h]

  puts("crack-me for Root-me by s4r");
  puts("Enter password please");
  fgets(v5, 64, stdin);
  v5[strlen(v5) - 1] = 0;
  if ( strlen(v5) != 19 )
    goto LABEL_21;
  for ( i = 8; i < 17; ++i )
  {
    if ( v5[i] != 105 )
      goto LABEL_21;
  }
  if ( v11 == 115
    && v10 == 112
    && v9 == 109
    && v5[2] == 110
    && v8 == 110
    && v5[0] == 99
    && v5[1] == 97
    && v5[3] == 116
    && v6 == 114
    && v7 == v6 + 3 )
  {
    correct();
  }
  else
  {
LABEL_21:
    failed();
    v12 = 0;
    return 0;
  }
  return v13;
}
```
- Analyze the above code. The password must have 19 characters and the element from position 8 to 16 must have an ASCII code of 105. Next, the remaining elements are compared with the ASCII codes one by one.
- Processing each part, first with elements from 8 to 16, they must be the character sequence __"iiiiiiiii"__
- Next
```python
v5_0 = chr(99)          # c
v5_1 = chr(97)          # a
v5_2 = chr(110)         # n
v5_3 = chr(116)         # t
v6 = chr(114)           # r
v7 = chr(ord(v6) + 3)   # u
v8 = chr(110)           # n
v9 = chr(109)           # m
flag8_16 = "iiiiiiii"   # iiiiiiii
v10 = chr(112)          # p
v11 = chr(115)          # s
```
- Combined, the password will be: `cantrunmiiiiiiiiips`
`🚩Flag: cantrunmiiiiiiiiips`