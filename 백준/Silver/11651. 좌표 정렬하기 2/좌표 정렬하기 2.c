#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
  int *pa = (int *)a;
  int *pb = (int *)b;

  if (pa[1] != pb[1]) return pa[1] - pb[1];   
  else return pa[0] - pb[0];                  
}

int main(void) {
  int n;
  scanf("%d", &n);

  int arr[100000][2];

  for (int i = 0; i < n; i++) {
    scanf("%d %d", &arr[i][0], &arr[i][1]);
  }

  qsort(arr, n, sizeof(arr[0]), compare);

  for (int i = 0; i < n; i++) {
    printf("%d %d\n", arr[i][0], arr[i][1]);
  }

  return 0;
}