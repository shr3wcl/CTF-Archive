# Source

ssh col@pwnable.kr -p2222 (pass: guest)

```c
#include <stdio.h>
#include <string.h>
unsigned long hashcode = 0x21DD09EC;
unsigned long check_password(const char* p){
        int* ip = (int*)p;
        int i;
        int res=0;
        for(i=0; i<5; i++){
                res += ip[i];
        }
        return res;
}

int main(int argc, char* argv[]){
        if(argc<2){
                printf("usage : %s [passcode]\n", argv[0]);
                return 0;
        }
        if(strlen(argv[1]) != 20){
                printf("passcode length should be 20 bytes\n");
                return 0;
        }

        if(hashcode == check_password( argv[1] )){
                system("/bin/cat flag");
                return 0;
        }
        else
                printf("wrong passcode.\n");
        return 0;
}
```

# 🚩POC

The program will compare the argument with __hashcode__ (has value is 0x21DD09EC). 
The code handle argument then after compare with __hashcode__:
```c
        int* ip = (int*)p;
        int i;
        int res=0;
        for(i=0; i<5; i++){
                res += ip[i];
        }
        return res;
```
The input value must be 20 bytes. Combine this with the code above so that we have to pass a data input of 20 characters and separated into 5 parts such that their sum is the value of the hashcode.

Compute this:
```python
A * 4 + B = 0x21DD09EC
```
So A = rounded(0x21DD09EC / 5)
And B = 0x21DD09EC - A * 4

```python
A = int(0x21DD09EC / 5) #  113626824  ==  0x6c5cec8
B = 0x21DD09EC - 4 * A  #  113626828  ==  0x6c5cecc
```
Input value will be: (Use little-edians)
```bash
./col "$(python2 -c "print '\xc8\xce\xc5\x06' * 4 + '\xcc\xce\xc5\x06'")" 
```

Run payload on server:
```bash
col@pwnable:~$ ./col "$(python2 -c "print '\xc8\xce\xc5\x06' * 4 + '\xcc\xce\xc5\x06'")"
daddy! I just managed to create a hash collision :)
```

Flag is: ___daddy! I just managed to create a hash collision :\)___