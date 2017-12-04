#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


void vuln(){
    char buffer[0x44];
    int* i=(int*)&buffer[0x40];
    puts("Don't overflow me,please....LOL...");
    for(*i=0;*i!=0x41;*i=*i+1){
        read(0,buffer+*i,1);
        if(buffer[*i]=='\n')break;
    }
}

int main(){
    setvbuf(stdin,0,2,0);
    setvbuf(stdout,0,2,0);
    setvbuf(stderr,0,2,0);
    vuln();
    return 0;
}
