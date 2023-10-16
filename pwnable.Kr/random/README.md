# Source

Daddy, teach me how to use random value in programming!

ssh random@pwnable.kr -p2222 (pw:guest)

[Code](./random.c)

# Solve

Connect to SSH and create a new C code file.
```c
#include<stdio.h>
int main(){
    unsigned int random;
    random = rand();
    printf("%u", random);
}
```
Compile and run the code above, we have the result:
```bash
random@pwnable:/tmp/temppp$ gcc a.c
a.c: In function ‘main’:
a.c:5:14: warning: implicit declaration of function ‘rand’ [-Wimplicit-function-declaration]
     random = rand();
              ^
random@pwnable:/tmp/temppp$ ./a.out
1804289383
random@pwnable:/tmp/temppp$ ./a.out
1804289383
random@pwnable:/tmp/temppp$ ./a.out
1804289383
random@pwnable:/tmp/temppp$
```

Value of rand() always is 1804289383. So __random__ has value is 1804289383. We just need to find value of __key__, then we can bypass this challenge.

__key = 0xdeadbeef ^ random = 0xdeadbeef ^ 1804289383 = 3039230856__

Run the binary file on server and pass in value of __key__.
```bash
random@pwnable:~$ ./random
3039230856
Good!
Mommy, I thought libc random is unpredictable...
random@pwnable:~$
```

Flag: ___Mommy, I thought libc random is unpredictable...___