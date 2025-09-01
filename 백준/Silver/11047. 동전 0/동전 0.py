n, k = map(int, input().split())
coins = []
for i in range(n):
  coins.append(int(input()))
min = 0
for i in range(n-1, -1, -1):
  if k >= coins[i]:
    min += k // coins[i]
    k %= coins[i]
    if k == 0:
      break
print(min)
