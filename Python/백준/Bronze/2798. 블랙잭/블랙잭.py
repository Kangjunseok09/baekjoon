n, m = map(int, input().split())
a = list(map(int, input().split()))
result = []
for i in range(n):
  for j in range(i+1, n):
    for k in range(j + 1, n):
      if a[i] + a[j] + a[k] == m:
        result.append(m)
      elif a[i] + a[j] + a[k] < m:
        result.append(a[i] + a[j] + a[k])

print(max(result))