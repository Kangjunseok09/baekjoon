#include<stdio.h>

int main(void){
  char s[101];
  int cnt = 0;
  scanf("%s", s);
  for (int i = 0; s[i] != '\0'; ){
    if(s[i] == 'c' && s[i+1] == '='){
      i += 2;
    }else if(s[i] == 'c' && s[i+1] == '-'){
      i += 2;
    }else if(s[i] == 'd' && s[i+1] == 'z' && s[i+2] == '='){
      i += 3;
    }else if(s[i] == 'd' && s[i+1] == '-'){
      i += 2;
    }else if(s[i] == 'l' && s[i+1] == 'j'){
      i += 2;
    }else if(s[i] == 'n' && s[i+1] == 'j'){
      i += 2;
    }else if(s[i] == 's' && s[i+1] == '='){
      i += 2;
    }else if(s[i] == 'z' && s[i+1] == '='){
      i += 2;
    }else{
      i++;
    }
    cnt++;
  }
  printf("%d\n", cnt);

  return 0;
}