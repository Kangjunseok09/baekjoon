#include<stdio.h>

int main(void){

  int n, arr[100001], top = 0, num, sum = 0;
  scanf("%d", &n);

  for(int i = 0; i < n; i++){
    scanf("%d", &num);
    if(num == 0){
      sum -= arr[--top];
    }else{
      sum += num;
      arr[top++] = num;
    }
  }
  printf("%d\n", sum);
  return 0;
}