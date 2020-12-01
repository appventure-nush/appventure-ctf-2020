#include <stdio.h>

int main() {
    int yay = 0;
    char buf[64];

    gets(buf);
    if (yay == 0xdeadbeef) {
        system("cat ./flag");
    } else {
        printf("try again");
    }
}
