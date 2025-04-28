result = []
x = True
while x:
  n = input()
  if n == '0':
    x = False
  elif n == n[::-1]:
    result.append("yes")
  else:
    result.append("no")

for i in range(len(result)):
  print(result[i])



