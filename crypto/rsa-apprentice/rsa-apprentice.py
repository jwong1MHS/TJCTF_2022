from math import lcm
from sympy.ntheory import primefactors


n = 1216177716507739302616478655910148392804849
e = 65537
c1 = 257733734393970582988408159581244878149116
c2 = 843105902970788695411197846605744081831851

factors = primefactors(n)
p = factors[0]
q = factors[1]
totient = lcm(p-1, q-1)
d = pow(e, -1, totient)
m1 = pow(c1, d, n)
m2 = pow(c2, d, n)
m1_bytes = hex(m1)[2:]
m2_bytes = hex(m2)[2:]
m1_string = bytes.fromhex(m1_bytes).decode("utf-8")
m2_string = bytes.fromhex(m2_bytes).decode("utf-8")
flag = m1_string + m2_string
print(flag)
