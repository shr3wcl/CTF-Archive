# Source

Mommy told me to make a passcode based login system.
My initial C code was compiled without any error!
Well, there was some compiler warning, but who cares about that?

ssh passcode@pwnable.kr -p2222 (pw:guest)

[Source](./passcode.c)

# Solve

- Vấn đề mà đoạn code này bị xuất hiện ở những đoạn code `scanf("%d", passcode...);`. Bởi vì tham số thứ hai của hàm này là một con trỏ tới địa chỉ cần nhập giá trị, nhưng tham số thứ hai lại được truyền vào là một số int. Vì vậy ở đây