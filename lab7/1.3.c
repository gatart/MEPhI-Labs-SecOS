#include <stdio.h>

extern char **environ;

int main(int argc, char *argv[]) {
    char **p;
    int i = 0;

    for (p = environ; *p != NULL && i < 10; p++, i++) {
         printf("%s\n", *p);
    }

    return 0;
}
