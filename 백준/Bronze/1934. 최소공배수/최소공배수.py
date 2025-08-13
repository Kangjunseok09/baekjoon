n = int(input())
for i in range(n):
  a, b = map(int, input().split())
  x, y = a, b
  while y != 0:
      x, y = y, x % y 

  print(abs(a * b) // x)