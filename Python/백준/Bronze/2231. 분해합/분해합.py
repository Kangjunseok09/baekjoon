n = int(input())
result = []
for i in range(1, n+1):
  a = str(i)
  if i + sum(map(int, a)) == n:
    result.append(i)

if result:
  print(min(result))
else:
  print(0)