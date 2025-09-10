#include<stdio.h>

int main(void){

  int k, a = 1, b = 0, temp;
  scanf("%d", &k);
  for(int i = 0; i < k; i++){
    temp = a;
    a = b;
    b += temp;
  }

  printf("%d %d\n", a, b);



  return 0;
}