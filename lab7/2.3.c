#include <stdio.h>
#include <unistd.h>

int main(void)
{
  int pid = fork();
  int i = 0;

  for(i = 0; i < 10; i++)
    if (pid > 0)
      fork();

  sleep(5);

  return 0;
}
