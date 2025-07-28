#include<stdio.h>
#include<math.h>

int main(void){
  int m, n;
  scanf("%d %d", &m, &n);
  int isprime[n+1];
  for(int i = 0; i < n+1; i++) isprime[i] = 0;
  isprime[0] = 1;
  isprime[1] = 1;

  for(int i = 0; i <= (int)sqrt(n); i++){
    if(isprime[i] == 0)
    for(int j = i*i; j < n+1; j+=i){
      isprime[j] = 1;
    }
  }

  for(int i = m; i < n+1; i++){
    if(!isprime[i]){
      printf("%d\n", i);
    }
  }
  return 0;
}