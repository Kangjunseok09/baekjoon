#include<stdio.h>

int main(void){
  int len = 0, tmp;
  char s[101];
  scanf("%s", s);

  while (s[len] != '\0'){
    len ++;
  }

  while (1){
    int changed = 0;
    for(int i = 0; i < len - 1; i++){
      if (s[i] < s[i+1]){
        tmp = s[i];
        s[i] = s[i+1];
        s[i+1] = tmp;
        changed = 1;
      }
    }
    if (changed == 0){
      break;
    }
  }
  

  printf("%s\n", s);

  return 0;
}