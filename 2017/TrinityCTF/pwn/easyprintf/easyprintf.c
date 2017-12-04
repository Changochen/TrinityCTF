#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

void init(){
    setvbuf(stdout,0,2,0);
    setvbuf(stderr,0,2,0);
    setvbuf(stdin,0,2,0);
}

void hacktheworld(){
    system("/bin/sh");
}

void fmt(){
    char buffer[0x30];
    memset(buffer,0,0x30);
    puts("Welcome to Ne0's format string vuln's demo.What's your name?");
    read(0,buffer,0x30);
    printf(buffer);
    puts("How about hacking the world?");
    read(0,buffer,0x30);
    printf(buffer);
}

int main(){
    init();
    fmt();
    puts("It seems that you failed...");
    return 0;
}
