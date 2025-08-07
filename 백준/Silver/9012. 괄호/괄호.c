#include<stdio.h>
#include<string.h>

int main(void){

  int n, cnt;
  char str[51];

  scanf("%d", &n);

  for(int i = 0; i < n; i++){
    scanf("%s", str);
    cnt = 0;
    for(int j = 0; j < strlen(str); j++){
      if (str[j] == '('){
        cnt++;
      }else if(str[j] == ')'){
        cnt--;
      }
      if(cnt < 0){
        printf("NO\n");
        break;
      }
    }
    if(cnt == 0){
      printf("YES\n");
    }else if(cnt > 0){
      printf("NO\n");
    }
  }

  return 0;
}