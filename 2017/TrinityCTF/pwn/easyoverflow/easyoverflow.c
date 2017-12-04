#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>

void vuln(){
    char s[0x10];
    char magic[0x10]="6666";
    read(0,s,0x14);
    if((*(unsigned int*) magic)==0xdeadbeef){
        printf("Shit!\n");
        system("/bin/sh");
    }
}


int main(){
    setvbuf(stdin,0,2,0);
    setvbuf(stdout,0,2,0);
    setvbuf(stderr,0,2,0);
    puts("Hello,babe.Are u ready to overflow me?");
    vuln();
    return 0;
}
