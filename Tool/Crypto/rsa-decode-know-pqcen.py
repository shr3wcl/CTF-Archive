from Cryptodome.Util.number import long_to_bytes,bytes_to_long 
import math
n = int(input("Enter n: "))          
c = int(input("Enter c: "))
e = int(input("Enter e: "))             

p = int(input("Enter p: "))             
q = int(input("Enter q: "))   

phi = (p-1)*(q-1)

d = pow(e,-1,phi)
flag = pow(c,d,n)
print("\n[+] Answer: " + long_to_bytes(flag))