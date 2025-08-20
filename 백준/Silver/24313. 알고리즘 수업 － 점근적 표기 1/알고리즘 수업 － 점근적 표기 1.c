#include <stdio.h>

int main(void) {
  long long a1, a0, c, n0;

  scanf("%lld %lld", &a1, &a0);
  scanf("%lld", &c);
  scanf("%lld", &n0);

  if (a1 <= c && a1 * n0 + a0 <= c * n0) {
      printf("1\n");
  } else {
      printf("0\n");
  }

  return 0;
}