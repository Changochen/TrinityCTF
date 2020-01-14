#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include <stdlib.h>
#include <alloca.h>
#include <fcntl.h>

unsigned long long key;
char buf[100];
char buf2[100];

static void init () {
  setvbuf (stdout, 0, 2, 0);
  setvbuf (stdin, 0, 1, 0);
}

void vuln () {
  char* args[3], **p = args;
  *p++ = "/bin/cat";
  *p++ = "flag";
  *p++ = 0;

  for (int i = 0; i < 4; i++) {
    printf ("Say something to me? (%d)\n", i + 1);
    read (0, buf, 100);
    printf (buf);
  }

  printf ("Don't brute force ...\n");
  sleep (3);

  printf ("Input the key : \n");
  read (0, buf2, 100);
  unsigned long long pw = strtoull (buf2, 0, 10);
  if (pw == key) {
    puts ("Congratulations! Here is the flag:");
    execve(args[0], args, 0);
  } else {
    puts ("Good luck next time!");
  }
}

int main () {
  init();
  int fd = open ("/dev/urandom", O_RDONLY);
  if (fd == -1 || read (fd, &key, 8) != 8) {
    srandom (time (NULL));
    key = random ();
  }
  close (fd);

  alloca (0xabcd & key);

  vuln ();
  return 0;
}
