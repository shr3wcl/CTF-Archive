# Solution

Chương trình sẽ lấy giá trị nhập từ người dùng (một số nguyên) rồi sau đó đem [XOR](https://vi.wikipedia.org/wiki/Ph%C3%A9p_to%C3%A1n_thao_t%C3%A1c_bit#XOR) từng ký tự trong một chuỗi **"\x22\x33\x20\x22\x2A\x2C\x24"** với nó rồi in kết quả ra màn hình.

Để giải quyết thử thách này, mình đã viết một [chương trình FUZZ bằng python](fuzz.py) để tìm ra key đúng.

Gồm có 2 key in ra chuỗi **"crackme"** và **"CRACKME"** là **65** và **97**. Đây có vẻ là chuỗi giá trị ban đầu mà tác giả muốn chúng ta tìm ra.
