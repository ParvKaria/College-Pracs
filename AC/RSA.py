import math

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"The modular inverse does not exist for {a} mod {m}")
    return x % m

p = int(input("Enter the value of p: "))
q = int(input("Enter the value of q: "))

n = p * q
phi = (p - 1) * (q - 1)

e = int(input(f"Choose e such that 1 < e < {phi} and e is coprime to {phi}: "))

d = mod_inverse(e, phi)

m = int(input("Enter the value of m: "))

ct = pow(m, e, n)
print("Cipher text is", ct)

dt = pow(ct, d, n)
print("Decrypted text is", dt)

print("\nPublic Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))