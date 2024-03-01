#include <stdio.h>

int main() {
    FILE *file;
    char ch;

    file = fopen("flag.enc", "r");
    if (file == NULL) {
        printf("Không thể mở tệp.\n");
        return 1;
    }

    while ((ch = fgetc(file)) != EOF) {
        ch = ch ^ 143; 
        printf("%c", ch);
    }

    fclose(file);

    return 0;
}
