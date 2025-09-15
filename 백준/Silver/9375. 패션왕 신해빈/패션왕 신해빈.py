n = int(input())
for i in range(n):
  c = int(input())
  clothes = {}
  result = 1
  for j in range(c):
    name, kind = input().split()
    if kind in clothes:
      clothes[kind] += 1
    else:
      clothes[kind] = 1
  for cnt in clothes.values():
    result *= (cnt + 1)
  print(result - 1)
