# Source

[Source](./ch23.bin)

# Solve

- File analysis:
```bash
$ checksec ch23.bin 
[*] '/home/Security/CTF/Rootme/Cracking/ELF ARM - Basic Crackme/ch23.bin'
    Arch:     arm-32-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8000)
```
- Disassembled using IDA 32bit, we have pseudocode of main function:
```c
void __fastcall __noreturn main(int a1, char **a2, char **a3)
{
  size_t status; // [sp+8h] [bp-1Ch]
  char *s; // [sp+Ch] [bp-18h]
  int v5; // [sp+14h] [bp-10h]
  int v6; // [sp+14h] [bp-10h]

  if ( a1 != 2 )
  {
    puts("Please input password");
    exit(1);
  }
  s = a2[1];
  printf("Checking %s for password...\n", s);
  status = strlen(s);
  if ( status != 6 )
  {
    puts("Loser...");
    exit(status);
  }
  v5 = 6 - strlen(s);
  if ( *s != s[5] )
    ++v5;
  if ( (unsigned __int8)*s + 1 != (unsigned __int8)s[1] )
    ++v5;
  if ( (unsigned __int8)s[3] + 1 != (unsigned __int8)*s )
    ++v5;
  if ( (unsigned __int8)s[2] + 4 != (unsigned __int8)s[5] )
    ++v5;
  if ( (unsigned __int8)s[4] + 2 != (unsigned __int8)s[2] )
    ++v5;
  v6 = v5 + ((unsigned __int8)s[3] ^ 0x72) + (unsigned __int8)s[6];
  if ( !v6 )
  {
    puts("Success, you rocks!");
    exit(0);
  }
  puts("Loser...");
  exit(v6);
}
```
- Analyzing the above code, the password must have 6 characters. These characters will then be compared with the remaining characters. Variable v5 will have the value 0, and after performing the comparison, variable v5 must still have a value of 0 for the password to be correct.
```c
  v5 = 6 - strlen(s);
  if ( *s != s[5] )
    ++v5;
  if ( (unsigned __int8)*s + 1 != (unsigned __int8)s[1] )
    ++v5;
  if ( (unsigned __int8)s[3] + 1 != (unsigned __int8)*s )
    ++v5;
  if ( (unsigned __int8)s[2] + 4 != (unsigned __int8)s[5] )
    ++v5;
  if ( (unsigned __int8)s[4] + 2 != (unsigned __int8)s[2] )
    ++v5;
  v6 = v5 + ((unsigned __int8)s[3] ^ 0x72) + (unsigned __int8)s[6];
```
- Focus on this code, and reverse compile to obtain the value of variable s (which is the password to find).
```python
s[3] = chr(0x72)            # r
s[0] = chr(0x72 - 1)        # s
s[5] = s[0]                 # s
s[1] = chr(ord(s[0]) + 1)   # t
s[2] = chr(ord(s[5]) - 4)   # o
s[4] = chr(ord(s[2]) - 2)   # m
print(s)                    # storms
```
- This is also the flag.

### 🚩Flag: `storms`