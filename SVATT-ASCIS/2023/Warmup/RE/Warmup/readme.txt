# Solution

- Dùng IDA để phân tích file này. Ở đây, mình sẽ chuyển về mã giả C để dễ dàng hơn cho việc phân tích (Dùng F5).
- Khi dùng IDA để phân tích, mình tập trung vào các hàm có chức năng đặc biệt liên quan đến thử thách.

- Mình sẽ chạy chương trình để nắm cơ bản về cách chương trình hoạt động trước khi bắt tay vào phân tích chương trình.

- Đầu tiên, với hàm **sub_140004D60**. Đây có lẽ là hàm có chức năng in ra màn hình - tương tự với **printf** trong C. Vì vậy, mình sẽ đổi tên hàm (Nhấn vào hàm và nhấn **N**) này thành printf để dễ dàng phân tích.
- Tiếp theo, với hàm **sub_1400050F0** - đây có thể là hàm được dùng để lấy dữ liệu từ người dùng tương tự như **scanf** trong C. Mình đổi tên thành **scanf**. -> Biến **v61** chính là biến lưu trữ đầu vào mà người dùng nhập.
-> Từ hàm này, mình cũng đã đoán ra được hàm **sub_140004150** có thể là hàm dùng để cấp phát bộ nhớ.

- Tiếp tục phân tích các dòng code tiếp theo.

```c
v44 = sub_140003D10(v61, v54, 0i64, 6i64);
v32 = 1;
v38 = 1;
if ( !(unsigned __int8)sub_140005140(v44, "ASCIS{") )
{
    v3 = unknown_libname_55(v61);
    v45 = sub_140003D10(v61, v53, v3 - 1, 1i64);
    v32 = 3;
    if ( !(unsigned __int8)sub_140005140(v45, "}") )
        v38 = 0;
}
```

- Ở đoạn code trên, dựa vào dòng code **if ( !(unsigned __int8)sub_140005140(v44, "ASCIS{") )** có thể hiểu được nó được dùng để kiểm tra kết quả so sánh giữa biến v44 và chuỗi ASCIS{. Nếu thỏa mã 2 chuỗi có giá trị giống nhau thì chương trình tiếp tục so sánh giá trị của biến v45 với chuỗi }. Ngay đây, mình nhận ra chương trình bắt chúng ta tìm ra và nhập FLAG để làm input đúng của chương trình với format là: **ASCIS{...}**
-> Mình đổi tên hàm **sub_140005140** thành strcmp để dễ dàng phân tích
- Từ hàm **sub_140005140** mình cũng có thể dễ dàng suy đoán hàm **sub_140003D10** có chức năng tương tự như **strcpy** - dùng để copy chuỗi chỉ định từ **Source** đến **Destination**. -> Đổi tên hàm **sub_140003D10** thành **strcpy**
- Từ logic chương trình và format của flag thì dễ dàng suy đoán **v3** là biến lưu trữ chiều dài của chuỗi người dùng nhập vào -> **unknown_libname_55** là hàm dùng để lấy chiều dài của chuỗi -> Đổi tên thành **strlen**

- Đoạn code trên trở thành như bên dưới

```c
Str1 = strcpy(Str, Source, 0i64, 6i64);
v32 = 1;
v38 = 1;
    if ( !(unsigned __int8)strcmp(Str1, "ASCIS{") )
    {
    v3 = strlen(Str);
    v45 = strcpy(Str, v53, v3 - 1, 1i64);
    v32 = 3;
    if ( !(unsigned __int8)strcmp(v45, "}") )
        v38 = 0;
}
```

- Tiếp tục đi đến đoạn code sau, chương trình lấy chuỗi bên trong flag và lưu vào trong biến v46

```c
v6 = strlen(Destination);
v46 = strcpy(Destination, v55, 6i64, v6 - 7);
```

- Đi vào trong hàm while, ở đoạn code bên dưới

```c
LOBYTE(v7) = 45;
v39 = sub_140003D70(Destination, v7, v43);
if ( v39 == -1 )
break;
LOBYTE(v8) = 45;
v43 = sub_140003DB0(Destination, v8, v39);
v47 = strcpy(Destination, v56, v39, v43 - v39);
sub_140003BB0(v60, v47);
```
- Chương trình gán giá trị 45 ('-') vào biến v7 và v8. Sau đó 2 biến này lại trở thành tham số cho hàm 
