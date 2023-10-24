# from secret import FLAG

HEX_CHARS = '0123456789abcdef'
B64_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


def from_hex(encoded):
    encoded = encoded.strip()
    if len(encoded) % 2 != 0:
        encoded = '0' + encoded
    data = 0
    for char in encoded:
        data <<= 4
        data += HEX_CHARS.index(char)
    return data.to_bytes((data.bit_length() + 7) // 8, 'big')


def from_base64(encoded):
    padding_length = encoded.count('=')
    encoded = encoded.replace('=', '')
    bits = ''.join([bin(B64_CHARS.index(c))[2:].zfill(6) for c in encoded])
    data = bytes(int(bits[i:i+8], 2) for i in range(0, len(bits), 8))
    return data[:-padding_length]


def main():
    with open('output.txt', 'r') as f:
        hex_encoded, base64_encoded = f.read().splitlines()

    first_half = from_hex(hex_encoded)
    second_half = from_base64(base64_encoded)

    FLAG = first_half + second_half

    print(FLAG)


main()