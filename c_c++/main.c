#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main()
{
    int a[3];
    for(int i = 0;i < 3;i++){
        scanf("%d",&a[i]);
        
    }
    
    for(int i = 0; i < 2; i++) {
        for(int j = 0; j < 2 - i; j++) {
            if(a[j] > a[j+1]) {
                int tmp = a[j];
                a[j] = a[j+1];
                a[j+1] = tmp;
            }
        }
    }
    printf("%d\n", a[1]);
    


     return 0;
}