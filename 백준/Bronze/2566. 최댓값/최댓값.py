alist = []
for i in range(9):
  alist.append(list(map(int, input().split())))
maxvalue = alist[0][0]
row = 1
span = 1

for i in range(9):
  for j in range(9):
    if alist[i][j] > maxvalue:
      maxvalue = alist[i][j]
      row = i + 1
      span = j + 1

print(maxvalue)
print(row, span)