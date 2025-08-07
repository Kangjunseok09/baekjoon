#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define OFFSET 4000
#define MAX 8001

int cmp(const void* a, const void* b) {
    return *(int*)a - *(int*)b;
}

int main() {
  int n, i, x, sum = 0, freq[MAX] = {0};
  int arr[500000];

  scanf("%d", &n);
  for (i = 0; i < n; i++) {
    scanf("%d", &x);
    arr[i] = x;
    sum += x;
    freq[x + OFFSET]++;
  }

  qsort(arr, n, sizeof(int), cmp);

  int max = 0, mode = 0, cnt = 0;
  for (i = 0; i < MAX; i++) {
    if (freq[i] > max) {
      max = freq[i];
      mode = i - OFFSET;
      cnt = 1;
    } else if (freq[i] == max && cnt == 1) {
      mode = i - OFFSET;
      cnt++;
    }
  }

  printf("%d\n", (int)round((double)sum / n));
  printf("%d\n", arr[n / 2]);
  printf("%d\n", mode);
  printf("%d\n", arr[n - 1] - arr[0]);

  return 0;
}