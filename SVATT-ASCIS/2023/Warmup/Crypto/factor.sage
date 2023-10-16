# Use online: https://sagecell.sagemath.org/

def crack_rsa(n, phi_n):
    R.<x> = PolynomialRing(QQ)
    f = x^2 - (n + 1 - phi_n) * x + n
    return [b for b, _ in f.roots()]

n = int(input("Enter n: "))
phi_n = int(input("Enter phi_n: ))
result = crack_rsa(n, phi_n)
print("[+] Result is: " + result)