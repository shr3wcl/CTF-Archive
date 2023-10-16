# Source

We all make mistakes, let's move on.
(don't take this too seriously, no fancy hacking skill is required at all)

This task is based on real event
Thanks to dhmonkey

hint : operator priority

ssh mistake@pwnable.kr -p2222 (pw:guest)

```c
#include <stdio.h>
#include <fcntl.h>

#define PW_LEN 10
#define XORKEY 1

void xor(char* s, int len){
        int i;
        for(i=0; i<len; i++){
                s[i] ^= XORKEY;
        }
}

int main(int argc, char* argv[]){

        int fd;
        if(fd=open("/home/mistake/password",O_RDONLY,0400) < 0){
                printf("can't open password %d\n", fd);
                return 0;
        }

        printf("do not bruteforce...\n");
        sleep(time(0)%20);

        char pw_buf[PW_LEN+1];
        int len;
        if(!(len=read(fd,pw_buf,PW_LEN) > 0)){
                printf("read error\n");
                close(fd);
                return 0;
        }

        char pw_buf2[PW_LEN+1];
        printf("input password : ");
        scanf("%10s", pw_buf2);

        // xor your input
        xor(pw_buf2, 10);

        if(!strncmp(pw_buf, pw_buf2, PW_LEN)){
                printf("Password OK\n");
                system("/bin/cat flag\n");
        }
        else{
                printf("Wrong Password\n");
        }

        close(fd);
        return 0;
}
```

# 🚩 Solve

Recreate the above code with the xor function and enter an input to find out the remaining input 2

```c
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
```
Input 1: AAAAAAAAAA 
Input 2: @@@@@@@@@@

```bash
mistake@pwnable:~$ ./mistake
do not bruteforce...
AAAAAAAAAA
@@@@@@@@@@
input password : Password OK
Mommy, the operator priority always confuses me :(
mistake@pwnable:~$
```

So, flag is: ___Mommy, the operator priority always confuses me :\(___