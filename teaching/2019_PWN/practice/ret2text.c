#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void secure() {
  int input;
  int secretcode;

  srand(time(NULL));
  secretcode = rand();
  scanf("%d", &input);
  if (input == secretcode)
    system("/bin/sh");
}

int main() {
  char buf;

  setvbuf(stdout, 0, 2, 0);
  setvbuf(stdin, 0, 1, 0);
  puts("There is something amazing here, do you know anything?");
  gets((char *)&buf);
  printf("Maybe I will tell you next time!");
  return 0;
}
