#include<stdio.h>

int main(void){

  int n, m, sum = 0;
  scanf("%d %d", &n, &m);
  int arr[n + 1];       
  int prefix[n + 1];    

  prefix[0] = 0;        
  for (int i = 1; i < n+1; i++) {
    scanf("%d", &arr[i]);
    prefix[i] = prefix[i - 1] + arr[i];
  }

  for (int k = 0; k < m; k++) {
    int i, j;
    scanf("%d %d", &i, &j);
    printf("%d\n", prefix[j] - prefix[i - 1]);
  }

  return 0;
}