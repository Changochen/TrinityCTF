#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

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

int main() {
    init();
    int d;
    puts("Feed me deadbeef!");
    read(0, &d, sizeof(d)); 
    if (d == 0xdeadbeef) {
        getflag();
    } else {
        goodluck();
    }
}
    
