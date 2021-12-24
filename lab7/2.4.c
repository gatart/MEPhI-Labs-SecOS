#include <stdio.h>
#include <unistd.h>

int main(void)
{
  int pid = fork();
  int i = 0;

  for(i = 1; 1 == 1; i++)
    if (pid > 0){
      fork();
      printf("Child process %d\n", i);
    }

  // I saw message "Child process 1450" and more, so I can suppose that there is no limitation or its too big to wait.

  sleep(5);

  return 0;
}
