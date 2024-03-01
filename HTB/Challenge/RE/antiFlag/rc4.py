def ksa(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]  # Swap
    return S

def prga(S, n):
    i = 0
    j = 0
    key = []
    for _ in range(n):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # Swap
        key.append(S[(S[i] + S[j]) % 256])
    return key

def rc4_encode(data, key):
    S = ksa(key)
    keystream = prga(S, len(data))
    encoded = bytearray()
    for i in range(len(data)):
        encoded.append(data[i] ^ keystream[i])
    return bytes(encoded)

def rc4_decode(data, key):
    return rc4_encode(data, key) 

data = b"\xD0\xc0\x35\x4f\x0c\xd9\x23\x2a\x48\x4b\x09\x0b\x54\x3c\xf8\xc0\xe5\xdf\xd7\x79\x0f\x3d\xdb\x35\xc4"
key = b"2asdf-012=14"

# # Mã hóa dữ liệu
# encoded_data = rc4_encode(data, key)
# print("Encoded data:", encoded_data)

# Giải mã dữ liệu
decoded_data = rc4_decode(data, key)
print("Decoded data:", decoded_data.decode())
