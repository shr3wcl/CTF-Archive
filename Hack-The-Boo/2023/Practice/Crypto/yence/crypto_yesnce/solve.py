from Cryptodome.Util import Counter
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Cipher import AES
import os

with open('messages.txt') as f:
    MSG = eval(f.read())

class AdvancedEncryption:
    def __init__(self, block_size):
        self.KEYS = self.generate_encryption_keys()
        self.CTRs = [Counter.new(block_size, initial_value=i) for i in range(len(MSG))]

    def generate_encryption_keys(self):
        keys = [[b'\x00'] * 16 for _ in range(len(MSG))]

        for i in range(len(keys)):
            for j in range(16):
                keys[i][j] = os.urandom(1)

        return keys

    def encrypt(self, i, msg):
        key = b''.join(self.KEYS[i])
        ctr = self.CTRs[i]
        cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
        return cipher.encrypt(pad(msg.encode(), 16))

    def decrypt(self, i, ciphertext):
        key = b''.join(self.KEYS[i])
        ctr = self.CTRs[i]
        cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
        decrypted = cipher.decrypt(ciphertext)
        return unpad(decrypted, 16).decode()
    
def main():
    AE = AdvancedEncryption(128)
    with open('output.txt', 'r') as f:
        ciphertexts = f.readlines()
        for i in range(len(ciphertexts)):
            ct = bytes.fromhex(ciphertexts[i].strip())
            decrypted = AE.decrypt(i, ct)
            print(f"Decrypted message {i+1}: {decrypted}")

if __name__ == '__main__':
    main()