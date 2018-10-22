#include <stdio.h>
#include <unistd.h>


int main(){
    char buf[0x100];

    read(0,buf,0x100);

    write(1,buf,0x100);

    return 0;
}
