#include <stdio.h>
#include <unistd.h>

int main(void)
{
  int pid = fork();

  if (pid == 0) {
    printf("Это сообщение из дочернего процесса\n"
           "Parent PID: %d\nChild PID: %d\n", getppid(),getpid());
  } else if (pid > 0) {
    printf("Это сообщение из родительского процесса.\n"
           "Идентификатор дочернего процесса:  %d\n", pid);
  }

  sleep(5);

  return 0;
}
