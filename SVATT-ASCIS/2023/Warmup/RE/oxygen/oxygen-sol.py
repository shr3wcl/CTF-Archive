# string = b'n[}>}C]qRm['
# result = ''
# for x in range(len(string)):
#     for eax in range(256):
#         if x%2==0:
#             if (eax | 0x0A) - (eax& 0x0A) == string[x]:
#                 result += chr(eax)
#         else:
#             if(eax|0x0A)+(eax&0x0A) == string[x]:
#                 result += chr(eax)
# print(result)
a = "Z[\v\n^_"
flag = ""
for i in a:
    flag += chr(ord(i) ^ 0x69)
print(flag)

# ASCIS{829872-bccd38-3e2960-783f8d-63d824-32bc76}