#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <string.h>
#include <unistd.h>

static void __attribute__((constructor)) pre_main1(void)
{
    char *addr=(char*)0x400000;
    mprotect((void*)addr,0x1000,PROT_READ|PROT_WRITE|PROT_EXEC);
    for(int i=0;i<0x94;i++){
        addr[0x685+i]^=0x33;
    }
    mprotect((void*)addr,0x1000,PROT_READ|PROT_EXEC);
}

int main(void)
{   char buffer[0x20];
    int i;
    read(0,buffer,0x20);
    for(i=0;i<0x10;i++){
        if(buffer[i]!=(i*i+0x66)){
            break;
        }
    }

    if(i!=0x10){
        puts("Try again:(");
    }else{
        puts("Congradulation!");
    }
    return 0;
}
