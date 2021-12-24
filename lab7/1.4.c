#include <stdio.h>
#include <stdlib.h>

extern char **environ;

int main(int argc, char *argv[]) {
    char **p;
    int i = 0;

    if (argc < 2)
        return 1;

    int max = atoi(argv[1]);

    for (p = environ; *p != NULL && i < max; p++, i++) {
         printf("%s\n", *p);
    }

    return 0;
}
