n, k = map(int, input().split())

arr = [0] * (n+1)
cnt = 0
for i in range(2, n+1):
  for j in range(i, n+1, i):
    if arr[j] == 0:
      arr[j] = 1
      cnt += 1
      if cnt == k:
        print(j)
        exit()

