from Cryptodome.Util.number import *
from sympy.ntheory.modular import crt

c_p = int(input("Enter c_p: "))
c_q = int(input("Enter c_q: "))
N = int(input("Enter N: "))
phi = int(input("Enter phi: "))
e = int(input("Enter e: "))


p = int(input("Enter p: "))
q = int(input("Enter q: "))

assert isPrime(p) == True 
assert isPrime(q) == True
assert p * q == N
d = inverse(e, phi)

mp = pow(c_p, d % (p - 1), p)
mq = pow(c_q, d % (q - 1), q)

m1, m2 = crt([p, q], [mp, mq])
print("\n[+] Answer: " + long_to_bytes(m1).decode())