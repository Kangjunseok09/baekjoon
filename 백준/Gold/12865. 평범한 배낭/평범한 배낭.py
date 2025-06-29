n, k = map(int, input().split())

backpack = [tuple(map(int, input().split())) for _ in range(n)]

dp = [0] * (k + 1)

for x, y in backpack:
    for i in range(k, x - 1, -1):  
        dp[i] = max(dp[i], dp[i - x] + y)

print(dp[k])