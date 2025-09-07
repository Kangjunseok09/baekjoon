#include<stdio.h>

int main(void){

  int t, n, count0[41], count1[41];
  count0[0] = 1; count0[1] = 0;
  count1[0] = 0; count1[1] = 1;
  scanf("%d", &t);
  for(int i = 2; i < 41; i++){
    count0[i] = count0[i-1] + count0[i-2];
    count1[i] = count1[i-1] + count1[i-2];
  }

  for(int i = 0; i < t; i++){
    scanf("%d", &n);
    printf("%d %d\n", count0[n], count1[n]);
  }
  
  return 0;
}