#include <stdio.h>
#include <stdlib.h>

char buf[2048];

int main(int argc, char **argv) {
    FILE *fp = fopen("/flag", "r");
    fgets(buf, 2048, fp);
    printf("%s\n", buf);
}
