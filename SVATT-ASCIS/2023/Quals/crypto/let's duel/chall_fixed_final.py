from hashlib import *
import os
from Crypto.Util.number import *


q = 2^32 - 5
n = 256
def bytes_to_seedlist(seedbytes):
    seedlist = []
    for i in range(16):
        seedlist.append(bytes_to_long(seedbytes[i*4:i*4+4]))
    return seedlist

def sample_poly(seed , lower , upper):
    prng = PRNG(seed)
    polylist = []
    for i in range(n):
        polylist.append((prng.raw_rand() % (upper - lower)) + lower)
    return polynomial(polylist)
def encode_m(m):
    m = bytes_to_long(m)
    flist = []
    for i in range(n):
        flist = [m&1] + flist
        m >>= 1
    return polynomial(flist)

class PRNG:
    def __init__(self , seed):
        self.state = bytes_to_seedlist(seed)
        
        self.m = 8723550600886591460
        # f = [randint(0 , self.m) for _ in range(16)]
        self.f = [385590684360, 111617452318, 131804337312, 300824916689, 419524791075, 690238874924, 160408772216, 63764520785, 50573686124, 688400902026, 333066488215, 270710580449, 107293144053, 703516825252, 541402940593, 624566048630]
        self.d = 16
        for i in range(self.d):
            self.generate()
    def generate(self):
        res = 0
        for i in range(self.d):
            res += self.f[i] * self.state[i]
            res %= self.m
        self.state = self.state[1:] + [res]
    def raw_rand(self):
        temp = self.state[0]
        self.generate()
        return temp

class polynomial:
    def __init__(self,flist):
        n = 256
        if type(flist) == list:
            assert len(flist) == n
            self.f = [flist[i] % q for i in range(n)]

    def __add__(self , other):
        assert type(other) == polynomial
        return polynomial([(self.f[i] + other.f[i])%q for i in range(n)])
    def __sub__(self , other):
        assert type(other) == polynomial
        return polynomial([(self.f[i] - other.f[i])%q for i in range(n)])
    def __mul__(self , other):
        assert type(other) == polynomial
        res = [0 for _ in range(n)]
        for i in range(n):
            for j in range(n-i):
                res[i+j] += self.f[i] * other.f[j]
                res[i+j] %= q
        for j in range(1, n):
            for i in range(n-j, n):
                res[i+j-n] -= (self.f[i] * other.f[j])
                res[i+j-n] %= q
        return polynomial(res)

flag = b'<REDACTED>'
assert flag[:8] == b'ASCIS{it' and flag[-1:] == b'}' and len(flag) == 32
print(f'hash_list: {list(map(lambda x: sha256(x).digest(), [flag[i:i+5] for i in range(0, len(flag), 5)][:-1]))}')

A = sample_poly(os.urandom(64) , 0 , 2**32 - 5)
e = sample_poly(os.urandom(64) , -4 , 4)
s = encode_m(flag)
b = A*s + e
print(b.f)
print(A.f)