# Solution

Khi dùng IDA để phân tích chương trình

```c
v7 = 100;
v6 = 14;
v4 = 0;
v5 = 0;
puts("Welcome to the wonderful world of assembly!");
printf("Qual o numero magico? ");
__isoc99_scanf("%d", &v4);
v5 = (3 * v7 + v6) / v7;
if ( v5 == v4 )
puts("Essa eh a sua flag!");
else
puts("Try harder...");
return 0;
```

Chương trình sẽ thực hiện phép tính: **(3 * v7 + v6) / v7** rồi lưu vào **v5**. Cuối cùng so sánh **v5** với giá trị nguyên mà người dùng nhập vào.
Vậy giá trị đúng mà chúng ta cần nhập vào là: **(int)(3 * 100 + 14) / 100 = 3**
