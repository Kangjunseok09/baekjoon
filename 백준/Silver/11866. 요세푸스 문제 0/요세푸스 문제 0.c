#include<stdio.h>

int main(void){

  int n, k, i = 1;
  scanf("%d %d", &n, &k);
  int arr[n+1];
  for(int i = 1; i < n + 1; i++) arr[i] = 1;

  printf("<");
  int cnt = 0;
  int cnt_k = 0;

  while (1){
    if(arr[i] == 1) cnt_k++;
    if(arr[i] == 1 && cnt_k == k){
      cnt_k = 0;
      arr[i] = 0;
      cnt++;
      if(cnt == n){
        printf("%d>", i);
        break;
      }
      printf("%d, ", i);
    }
    i++;
    if(i>n) i = i - n;
  }
  

  return 0;
}