#include <unistd.h>
#include <string.h>

int puts(const char * s){
    write(1,"GOGOGO\n",7);
    write(1,s,strlen(s));
    write(1,"GOGOGO\n",7);
    return 0;
}
