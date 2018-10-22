#!/usr/bin/env python
# coding=utf-8
from pwn import *

f=open("./code",'rb')
code=f.read()

final=[0xc4,0x34,0x22,0xb1,0xd3,0x11,0x97,0x7,0xdb,0x37,0xc4,0x6,0x1d,0xfc,0x5b,0xed,0x98,0xdf,0x94,0xd8,0xb3,0x84,0xcc,0x8]

i = 14997

while i>=0:
    v0 = code[i]
    v3 = code[i+2]
    if v0== '\x01':
        final[u8(code[i+1])]-= u8(v3)
    elif v0=='\x02':
        final[u8(code[i+1])]+= u8(v3)
    elif v0=='\x03':
        final[u8(code[i+1])]^= u8(v3)
    elif v0=='\x04':
        final[u8(code[i+1])]/= u8(v3)
    elif v0=='\x05':
        final[u8(code[i+1])]^= final[u8(v3)]
    
    final[u8(code[i+1])]&=0xff
    i-=3

print(''.join([str(chr(i%128))for i in final]))
