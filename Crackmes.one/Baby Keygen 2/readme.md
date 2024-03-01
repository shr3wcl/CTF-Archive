# Solution

Khi dùng IDA để phân tích chương trình, thì với đoạn code sau mình có thể biết được keygen có độ dài năm trong 4 đến 9

```c
if ( length > 9 || length <= 3 )
  {
    printf("\nKey is not the right length");
    printf("\nLength is %d\n", (unsigned int)length);
    sleep(5i64);
    exitCode = -1;
  }
```

Tiếp tục sau đoạn code trên, có một logic code nữa thực hiện việc kiểm tra key

```c
else if ( user_input[0] == 116 && user_input[4] == 45 )
  {
    obtainedkey = hiddenKey();
    printf("KEY VALID: The pass is %s%d", obtainedkey, (unsigned int)i);
    sleep(5i64);
  }
```

Đoạn code này có nghĩa là ký tự ở vị trí 0 phải là **'t'** (Mã ASCII là 116) và vị trí 4 là **'-'** (Mã ASCII là 45)
Trong đoạn code này, nếu đúng logic thì có sẽ thực hiện việc gọi đến hàm **hiddenKey()** để in ra **Password**.

Từ đây, với mọi dữ kiện thì mình đã viết một chương trình Python để generate ra **KEY hợp lệ**. [Chương trình](keygen.py)
