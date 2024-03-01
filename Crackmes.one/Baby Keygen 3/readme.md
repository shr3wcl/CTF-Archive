# Solution

Oke, với thử thách này nhiệm vụ của chúng ta vẫn giống với thử thách trước là tìm cách tạo ra Key hợp lệ.
Đầu tiên, dùng IDA để phân tích chương trình được cung cấp thì mình phát hiện được đoạn code để kiểm tra Key

```c
key1 = get_user_input();
strcpy(user_input, key1);
magic = valid_key(user_input);
key2 = get_user_input();
strcpy(user_input, key2);
valid = valid_key(user_input);
magic += valid;
key3 = get_user_input();
strcpy(user_input, key3);
v4 = valid_key(user_input);
magic += v4;
if ( magic == 3 )
givepass();
```

Từ đoạn code trên, ta biết được chúng ta phải nhập 3 Key (có thể giống nhau bởi vì nó đều gọi đến một hàm là **valid_key** để kiểm tra KEY)

Tiếp tục phân tích hàm **valid_key**

```c
strcpy(localkey, key_to_valid);
if ( (unsigned int)strlen(localkey) == 11 )
{
if ( *localkey == 65 && localkey[3] == 45 && localkey[7] == 45 )
{
    printf("The key entered is valid");
    return 1;
}
else
{
    printf("I'm sorry but the key is wrong.");
    return -1;
}
}
else
{
printf("The size of the KEY you provided is not valid.");
return -1;
}
```

Đoạn code trên của hàm **valid_key** lấy KEY được nhập vào đem đi kiểm tra độ dài của nó có phải là **11** hay không .Sau đó, kiểm tra 3 phần tử ở vị trí **0**, **3** và **7** với lần lượt là **65** (A), **45** (-) và **45** (-).
Từ đây, chúng ta đã biết được logic để kiểm tra KEY. Bây giờ, mình đã viết chương trình gen các key hợp lệ [chương trình](keygen.py)
