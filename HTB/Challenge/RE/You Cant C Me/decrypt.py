s1 = "this_is_the_password"
v5 = "m^&&fi\x17Uo&kUZ'ZUYUc)"
flag = "HTB{"

for i in range(0, 20, 1):
	flag += chr(ord(v5[i]) + 10)

flag += "}"
print(flag)
