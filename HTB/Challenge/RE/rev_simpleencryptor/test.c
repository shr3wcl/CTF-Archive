#include<stdio.h>
#include<time.h>
#include<stdlib.h>

int main(){
    int se = 1708266543;
    srand(se);
    int a = rand();
    printf("%d\n", a);
}