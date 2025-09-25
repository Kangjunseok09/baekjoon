#include<stdio.h>
#include<stdlib.h>

int compare(const void* a, const void* b){
  return(*(int*)a - *(int*)b);
}

int checkIn(int n, int size, int* arr){
  for(int i = 0; i < size; i++){
    if(n == arr[i]){
      return 1;
    }
  }
  return 0;
}


int main(void){

  int n, value, len = 0;
  scanf("%d", &n);
  int arr[n];
  while (len < n){
    scanf("%d", &value);
    if (!checkIn(value, len, arr)){
      arr[len++] = value; 
    }else{
      n --;
    }
  }
  qsort(arr, len, sizeof(int), compare);

  for (int i = 0; i < len; i++){
    printf("%d ", arr[i]);
  }



  return 0;
}