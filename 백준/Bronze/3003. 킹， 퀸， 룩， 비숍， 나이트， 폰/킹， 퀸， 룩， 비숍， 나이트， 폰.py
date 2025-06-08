chess = [1, 1, 2, 2, 2, 8]
result = []
input = list(map(int, input().split()))

for i in range(6):
  result.append(chess[i]-input[i])

for i in result:
  print(i, end=" ")