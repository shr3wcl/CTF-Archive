# Solution

Tương tự với thử thách [Baby Crackme](../Baby%20Crackme/), tuy nhiên tác giả đã thay XOR thành một thuật toán mã hóa là [Caesar](https://vi.wikipedia.org/wiki/M%E1%BA%ADt_m%C3%A3_Caesar) (Chương trình sẽ lấy chuỗi bí mật - ở đây là **Nkrru&Ngiqkxy**, từng phần tử đem trừ đi giá trị được người dùng nhập vào rồi in ra màn hình).

Để giải quyết thử thách này, mình cũng đã viết một [chương trình Python để FUZZ](fuzz.py) ra giá trị key đúng.

Mình đã tìm ra 1 key là **6** với văn bản in ra là: **Hello Hackers**
