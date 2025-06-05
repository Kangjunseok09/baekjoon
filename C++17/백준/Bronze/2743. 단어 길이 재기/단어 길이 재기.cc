#include<stdio.h>

int main(void){
  int i = 0;
  char string[100];
  scanf("%s", string);
  while (string[i] != '\0'){
    i++;
  }
  printf("%d\n", i);
  return 0;
}