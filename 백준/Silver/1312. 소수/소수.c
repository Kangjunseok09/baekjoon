#include<stdio.h>

int main(void){

  int a, b, n, digit;
  scanf("%d %d %d", &a, &b, &n);
  for(int i = 0; i < n; i++){
    a = (a % b) * 10;
    digit = a / b;
  }
  printf("%d\n", digit);

  return 0;
}