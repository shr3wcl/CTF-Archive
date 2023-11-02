from Crypto.Random.random import getrandbits
from Crypto.Util.number import bytes_to_long

nbits = 128
while True:
    mul = getrandbits(nbits)
    add = getrandbits(nbits)
    modulus = getrandbits(nbits)
    if mul < modulus and add < modulus:
        break

def gen_num(bits):
    truncate = bits
    seed = getrandbits(511)
    gen_num = 41

    xx = []
    yy = [] 
    
    for _ in range(gen_num):
        seed = (mul * seed + add) % modulus
        xx.append(seed)
        yy.append(seed >> (nbits-truncate))
    return xx, yy

_, ee = gen_num(18)
_, ff = gen_num(20)

a = ee[-1]
b = ff[-1]
c = getrandbits(1024)
p = next_prime(a * c + getrandbits(512))
q = next_prime(b * c + getrandbits(512))

flag = '<REDACTED>'
N = p * q
e = 65537
m = bytes_to_long(flag.encode())
enc = pow(m, e, N)

print(f'enc = {enc}')
print(f'N = {N}')
print(f'ee = {ee[:-1]}')
print(f'ff = {ff[:-1]}')
print(f'a = {mul}')
print(f'c = {add}')
print(f'm = {modulus}')