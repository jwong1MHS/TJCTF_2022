# crypto

## ****rsa-apprentice****

`n=1216177716507739302616478655910148392804849` and `e=65537`. 

Factor using [factordb.com](http://factordb.com/).

Totient is `lcm(p-1, q-1)`.

Private key `d` is the modular multiplicative inverse of `e (mod totient)`

Code for `rsa-apprentice.py`:

```python
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
```

Flag: `tjctf{n0t_s0_S3cur3_Cryp70}`

## ******flimsy-fingered-latin-teacher******

Use the QWERTY keyboard for reference and look at the key to the left of each character.

`ykvyg}pp[djp,rtpelru[pdoyopm|` --> `tjctf{oopshomerowkeyposition}`

Flag: `tjctf{oopshomerowkeyposition}`

# forensics

## **fake-geoguessr**

Use `exiftool` to example the metadata of `lake.jpg`. Specifically, look at the Copyright and the Comment.

Flag: `tjctf{thats_a_lot_of_metadata}`

## **cool-school**

Use an online steganography solver like [Aperi'Solve.fr](https://www.aperisolve.fr/).

Flag: `tjctf{l0l_st3g_s0_co0l}`

## **spongebob**

Used an online Hidden Pixels decoder at [FotoForensics](https://fotoforensics.com/).

Flag: `tjctf{such_pogg3rs_ctf}`



sudo service --status-all

sudo service docker start

sudo systemctl enable docker

# misc

## twist-cord

first half of flag is in #announcements on discord: `tjctf{please_enjoy`

second half of flag is the first tweet on twitter: `_b6fd3b11fc5393c8}`

Flag: `tjctf{please_enjoy_b6fd3b11fc5393c8}`

# pwn

## **vacation-1**

![image-20220514065345332](C:\Users\jason\AppData\Roaming\Typora\typora-user-images\image-20220514065345332.png)

`0x7fffffffdfb8 - 0x7fffffffdfa0 = 24`

# web

## **lamb-sauce**

Inspect element at `lamb-sauce.tjc.tf` and look at the comment to find a hidden file at `/flag-9291f0c1-0feb-40aa-af3c-d61031fd9896.txt`, so redirect to `https://lamb-sauce.tjc.tf/flag-9291f0c1-0feb-40aa-af3c-d61031fd9896.txt`

Flag: `tjctf{idk_man_but_here's_a_flag_462c964f0a177541}`

