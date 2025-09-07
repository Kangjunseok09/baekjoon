#include<stdio.h>

int main(void){
  int n, k, cnt = 0;

  scanf("%d %d", &n, &k);
  int arr[n];
  for (int i = 0; i < n+1; i++) arr[i] = 0;

  for(int i = 2; i < n+1; i++){
    for(int j = i; j < n+1; j+=i){
      if(arr[j] == 0){
        arr[j] = 1;
        cnt ++;
        if(cnt == k){
          printf("%d\n", j);
          return 0;
        }
      }
    }
  }
}