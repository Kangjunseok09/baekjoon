n = int(input())
result = []
for i in range(n):
  R, S = input().split()
  R = int(R)
  resultadd = ""
  for j in S:
    resultadd += (j * R)
  result.append(resultadd)
for i in range(n):
  print(result[i])