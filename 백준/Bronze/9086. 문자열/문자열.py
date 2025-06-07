n = int(input())
result = []
for i in range(n):
  s = (input())
  result.append((s[0], s[len(s)-1]))

for i, j in result:
  print(i, j, sep="")
