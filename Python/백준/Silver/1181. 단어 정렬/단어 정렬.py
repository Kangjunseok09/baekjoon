n = int(input())
a = []
for i in range(n):
  a.append(input())
a = set(a)
a = list(a)
a.sort()
a.sort(key=len)
for i in a:
  print(i)