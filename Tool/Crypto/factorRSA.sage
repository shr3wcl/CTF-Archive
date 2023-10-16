# Use online: https://sagecell.sagemath.org/

def crack_rsa(n, phi_n):
    R.<x> = PolynomialRing(QQ)
    f = x^2 - (n + 1 - phi_n) * x + n
    return [b for b, _ in f.roots()]