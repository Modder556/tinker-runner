#include <stdio.h>
int main(void){
    printf("Hello from C on a real Linux VM\n");
    for (int i = 1; i <= 5; i++) printf("%d squared is %d\n", i, i*i);
    return 0;
}
