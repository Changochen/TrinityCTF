#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
void echo(char* string){
    char s[0x110];
    snprintf(s,0x100,"echo %s",string);
    system(s);
}
int main(){
    setvbuf(stdin,0,2,0);
    setvbuf(stdout,0,2,0);
    setvbuf(stderr,0,2,0);
    char* ptr=(char*)malloc(0x40);
    char temp[0x10];
    int d;
    int isfreed=0;
    char* input;
    strcpy(ptr,"Bye bye\n");
    while(1){
        puts("Hello,guy.Welcome to echo note system");
        puts("How long is your note?");
        scanf("%d",&d);
        if(d<0||d>0x1000){
            puts("Are you kidding me?");
            return -1;
        };
        input=(char*)malloc(d);
        puts("What do you want to say to us?");
        read(0,input,0x40);
        puts(input);
        puts("Do you want exit?");
        read(0,temp,0x10);
        if(temp[0]=='y'){
            break;
        }
        if(!isfreed)
        {
            isfreed=1;
            free(ptr);
            *ptr=0;
        }
        free(input);
    }
    puts("Okay,whatever you like\n");
    if(*ptr!=0)echo(ptr);
}
