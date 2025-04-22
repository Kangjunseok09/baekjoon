T = int(input())
solve = []
for i in range(T):
  result = 0
  count = 0
  a = input()
  for j in range(len(a)):
    if a[j] == "O":
      count += 1
      result += count
    elif a[j] == "X":
      count = 0
  solve.append(result)

for i in range(len(solve)):
  print(solve[i])