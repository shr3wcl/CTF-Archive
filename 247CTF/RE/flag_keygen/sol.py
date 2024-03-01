a = "BBBBBZBBBBBBBBAAAAAAAAAAAAOOOOOO"
for i in range(1, len(a), 1):
    c = a[i]
    if ord(a[i]) <= 77:
        c = ord(a[i]) + 181
    else:
        c = ord(a[i]) + 177
    print(c - i + 247)