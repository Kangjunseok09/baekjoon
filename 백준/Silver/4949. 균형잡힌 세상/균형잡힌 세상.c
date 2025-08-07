#include<stdio.h>
#include<string.h>

#define MAX 102

char stack[MAX];
int top = -1;

void push(char ch){
   stack[++top] = ch;
}

int pop(char ch){
   if(top == -1) return 0;
   if((ch == ')' && stack[top] != '(') || (ch == ']' && stack[top] != '[')) return 0;
   top --;
   return 1;
}

int judge(char* str){
   top = -1;
   for(int i = 0; i < strlen(str); i++){
      if((str[i] == '(') || (str[i] == '[')){
         push(str[i]);
      }else if ((str[i] == ')') || (str[i] == ']')){
         if(!pop(str[i])) return 0;
      }
   }
   return(top == -1);
}

int main(void){
   
   char arr[MAX];

   while(1){
      fgets(arr, sizeof(arr), stdin);

      if(arr[0] == '.' && (arr[1] == '\n' || arr[1] == '\0')) break;

      if(judge(arr)){
         printf("yes\n");
      }else{
         printf("no\n");
      }
   }

   return 0;
}
