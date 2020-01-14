#include <stdio.h>
#include <stdlib.h>

int main() {
  char buf[64];

  setvbuf(stdout, 0, 2, 0);
  setvbuf(stdin, 0, 1, 0);
  puts("This time, no system() and NO SHELLCODE!!!");
  puts("What do you plan to do?");
  gets(buf);
  return 0;
}
