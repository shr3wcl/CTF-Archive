# Source

Mom? how can I pass my input to a computer program?

ssh input2@pwnable.kr -p2222 (pw:guest)

[link](./input.c)

# Solve

- Ở bài này, thử thách chúng ta về việc truyền dữ liệu vào chương trình bằng các cách khác nhau.
- Tạo thư mục ở /tmp
- Payload: [Payload](./exploit.py)
- Tạo một symlink đến file flag gốc:
```bash
ln -s /home/input2/flag flag
```
`🚩Flag: Mommy! I learned how to pass various input in Linux :)`