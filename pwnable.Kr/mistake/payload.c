#include<stdio.h>

void xor (char *s, int len) {
    int i;
    for (i = 0; i < len; i++)
    {
        s[i] ^= 1;
    }
}

int main(){
    char a[10] = "AAAAAAAAAA";
    xor(a, 10);
    puts(a);
}