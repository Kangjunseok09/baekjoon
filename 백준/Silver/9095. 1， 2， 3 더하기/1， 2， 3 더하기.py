import sys
input = sys.stdin.readline
n = int(input())

def addCount(n):
  dp = [0] * (n+3)
  dp[1], dp[2], dp[3] = 1, 2, 4
  for i in range(4, n+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
  return dp[n]

for i in range(n):
  m = int(input())
  print(addCount(m))