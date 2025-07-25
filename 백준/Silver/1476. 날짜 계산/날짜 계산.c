#include<stdio.h>

int main(void){
  int e, s, m, year = 1;
  scanf("%d %d %d", &e, &s, &m);
  while (1){
    if (year % 15 == e % 15 && year % 28 == s % 28 && year % 19 == m % 19){
      break;
    }
    year++;
  }
  printf("%d\n", year);
  return 0;
}