#include<stdio.h>

int main(void){
  
  int a = 300, b = 60, c = 10, n;
  int acnt = 0, bcnt = 0, ccnt = 0;
  scanf("%d", &n);
  while (1){
    if(n >= a){
      acnt += n / a;
      n %= a;
    }else if (n >= b){
      bcnt += n / b;
      n %= b;
    }else if (n >= c){
      ccnt += n / c;
      n %= c;
    }else{
      break;
    }
  }
  if(n != 0){
    printf("%d\n", -1);
  }else{
    printf("%d %d %d\n", acnt, bcnt, ccnt);
  }

  return 0;
}