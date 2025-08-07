#include <stdio.h>

long long gcd(long long a, long long b) {
    while (b != 0) {
        long long temp = a % b;
        a = b;
        b = temp;
    }
    return a;
}

int main(void) {
    long long a, b;
    scanf("%lld %lld", &a, &b);

    long long g = gcd(a, b);
    long long lcm = (a / g) * b;

    printf("%lld\n", lcm);
    return 0;
}