#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>
#include <time.h>

#define PW_LEN 10
#define XORKEY 1

static void init() {
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 1, 0);
}

static void getflag() {
    puts("Congratulations! Here is the flag:");
    system("/bin/cat flag");
}

static void goodluck() {
    puts("Good luck next time!");
    exit(1);
}

void xor(char* s, int len){
    int i;
    for(i=0; i<len; i++){
        s[i] ^= XORKEY;
    }
}

int main(int argc, char* argv[]){
    init();
    int fd;
    if(fd = open("flag",O_RDONLY) < 0) {
        printf("Can't open flag\n");
        return 0;
    }

    printf("Do not bruteforce...\n");
    sleep(time(0)%10);

    char buf = 0;
    printf("Press Enter to continue...\n");
    while (read(0, &buf, 1) == 1 && buf != '\n');

    char pw_buf[PW_LEN+1];
    int len;
    if(!(len=read(fd,pw_buf,PW_LEN) > 0)){
        printf("Read error\n");
        close(fd);
        return 0;        
    }

    char pw_buf2[PW_LEN+1];
    printf("Input password : ");
    scanf("%10s", pw_buf2);

    xor(pw_buf2, 10);

    if(!strncmp(pw_buf, pw_buf2, PW_LEN)){
        getflag();
    }
    else{
        goodluck();
    }

    close(fd);
    return 0;
}

