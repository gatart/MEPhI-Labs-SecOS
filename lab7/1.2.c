#include <stdio.h>

extern char **environ;

int main(int argc, char *argv[]) {
    int vars = 0;
    char **p;

    for (p = environ; *p != NULL; p++) {
        vars++;
    }

    printf("Number of arguments: %d\nNumber of environment variables: %d\n", argc, vars);

    return 0;
}
