#include<stdio.h>
#include<stdlib.h>

int compare(const void* a, const void* b){
  return (*(int*)a - *(int*)b);
}

int main(void){
  int n, a, result = 0, befo = 0;
  scanf("%d", &n);
  int arr[n];
  for(int i = 0; i < n; i++){
    scanf("%d", &a);
    arr[i] = a;
  }
  qsort(arr, n, sizeof(int), compare);
  for(int i = 0; i < n; i++){
    befo += arr[i];
    result += befo;
  }

  printf("%d\n", result);

  return 0;
}