# Solution

Dùng IDA để phân tích thử thách này thì bạn có thể thấy ở hàm main có gọi đến 2 hàm lần lượt là **_Z7systemvv** và **_Z7systemov**.
Bắt đầu phân tích hàm **_Z7systemvv**. Ở hàm này, chương trình đưa các giá trị vào Stack tuy nhiên lại không LÀM SẠCH STACK (CLEAR) khi gọi RETURN. Cụ thể, chương trình gán giá trị 5 cho offset 4 và 7 cho offset 8.

```asm
push    rbp
mov     rbp, rsp
mov     [rbp+var_4], 5
mov     [rbp+var_8], 7
mov     [rbp+var_C], 1F5h
nop
pop     rbp
retn
```

Tiếp tục, mình phân tích hàm **_Z7systemov**. Hàm này sẽ lấy offset 4 và 8 của stack cộng lại với nhau (Ở đây với việc chưa clear stack như mình đã phân tích ở trên thì kết quả của việc này là: 12). Sau đó, chương trình lại đem kết quả nhân với 0x2D. 

```asm
mov     eax, [rbp+var_8]
add     [rbp+var_4], eax
mov     eax, [rbp+var_4]
imul    eax, 2Dh ; '-'
...
lea     rax, [rbp+var_10]
mov     rsi, rax
lea     rdi, _ZSt3cin@@GLIBCXX_3_4
call    __ZNSirsERi     ; std::istream::operator>>(int &)
mov     eax, [rbp+var_10]
cmp     eax, [rbp+var_C]
jnz     short loc_A62
```

Cuối cùng, giá trị này sẽ được đem đi so sánh với giá trị mà người dùng nhập vào, đây có nghĩa là nó - mật khẩu mà chúng ta cần tìm.

```math
12 * 0x2D = 540
```
