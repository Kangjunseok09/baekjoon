t= int(input())
def triangle(n):
  dp = [0] * (n + 3)
  dp[1] ,dp[2], dp[3] = 1, 1, 1
  for i in range(4, n+1):
    dp[i] = dp[i-3] + dp[i-2]
  return dp[n]
for i in range(t):
  n = int(input())
  print(triangle(n))


