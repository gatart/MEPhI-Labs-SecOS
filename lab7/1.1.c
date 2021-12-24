#include <stdio.h>

extern char **environ;

int main(int argc, char *argv[]) {
    int vars = 0;
    char **p;

    for (p = environ; *p != NULL; p++) {
        vars++;
    }

    printf("Number of environment variables: %d\n", vars);

    return 0;
}
