#include<stdio.h>

int main(void){

  int n, k, coin, min=0;
  scanf("%d %d", &n, &k);
  int coins[n];
  for(int i = 0; i < n; i++){
    scanf("%d", &coin);
    coins[i]=coin;
  }
  for(int i = n-1; i > -1; i--){
    if(k >= coins[i]){
      min += k / coins[i];
      k %= coins[i];
      if(k == 0){
        break;
      }
    }
  }

  printf("%d\n", min);


  return 0;
}