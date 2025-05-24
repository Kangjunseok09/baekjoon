n, m = map(int, input().split())
pocket = [0] * n
for _ in range(m):
  i, j, k = map(int, input().split())
  for __ in range(i-1,j):
    pocket[__] = k
for _ in pocket:
  print(_, end=" ")