#include<stdio.h>
#include<stdlib.h>

int compare(const void *a, const void *b){
    return (*(int*)a - *(int*)b);
}

int main(void){
    
    int arr[5], sum = 0;
    
    for(int i = 0; i < 5; i++){
        scanf("%d", &arr[i]);
        sum += arr[i];
    }
    
    qsort(arr, 5, sizeof(int), compare);
    
    printf("%d\n", sum / 5);
    printf("%d\n", arr[2]);
    
    
    
    
}