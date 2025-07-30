#include <stdio.h>
#include <string.h>

#define MAX 5001

char dp[10001][MAX];

void add(char *a, char *b, char *result) {
    int i = strlen(a) - 1;
    int j = strlen(b) - 1;
    int carry = 0, k = 0;
    char temp[MAX];

    while (i >= 0 || j >= 0 || carry) {
        int x = (i >= 0) ? a[i--] - '0' : 0;
        int y = (j >= 0) ? b[j--] - '0' : 0;
        int sum = x + y + carry;
        temp[k++] = (sum % 10) + '0';
        carry = sum / 10;
    }

    for (int t = 0; t < k; t++) result[t] = temp[k - t - 1];
    result[k] = '\0';
}

int main() {
    int n;
    scanf("%d", &n);

    strcpy(dp[0], "0");
    strcpy(dp[1], "1");

    for (int i = 2; i <= n; i++) {
        add(dp[i - 1], dp[i - 2], dp[i]);
    }

    printf("%s\n", dp[n]);
    return 0;
}