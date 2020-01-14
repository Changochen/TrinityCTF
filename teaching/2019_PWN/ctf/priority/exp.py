from pwn import *

p = process('./priority')

p.sendline()
p.sendline('0000000000')
p.sendline('1111111111')

print  p.recvall()
