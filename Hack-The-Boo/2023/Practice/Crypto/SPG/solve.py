from hashlib import sha256
import string, random
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad
from base64 import b64decode

ALPHABET = string.ascii_letters + string.digits + '~!@#$%^&*'

def decode_password(encoded_password):
    master_key = 0
    for i, char in enumerate(encoded_password):
        if char in ALPHABET[:len(ALPHABET)//2]:
            master_key |= (1 << i)

    return master_key.to_bytes((master_key.bit_length() + 7) // 8, 'little')

def main():
    with open('output.txt', 'r') as f:
        lines = f.readlines()

    password_line = lines[0]
    flag_line = lines[1]

    password = password_line.split(':')[1].strip()
    encoded_flag = flag_line.split(':')[1].strip()
    ciphertext = b64decode(encoded_flag)

    master_key = decode_password(password)
    encryption_key = sha256(master_key).digest()
    cipher = AES.new(encryption_key, AES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), 16)

    print(f"Decrypted Flag: {plaintext.decode()}")

main()