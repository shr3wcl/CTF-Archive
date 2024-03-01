#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "This is a sample string";
    char ch = 'a';
    size_t size = strlen(str);

    // Tìm ký tự 'a' trong chuỗi str
    char *result = memchr(str + 8, ch, size);

    if (result != NULL) {
        printf("Found '%c' at position: %ld\n", ch, result - str);
    } else {
        printf("'%c' not found.\n", ch);
    }

    return 0;
}
