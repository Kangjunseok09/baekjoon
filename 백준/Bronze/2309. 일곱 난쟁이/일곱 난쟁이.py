
sevenmini = []
for i in range(9):
  sevenmini.append(int(input()))

sevenmini.sort()
sum = sum(sevenmini) - 100
for i in range(8):
  for j in range(i+1, 9):
    if sevenmini[i] + sevenmini[j] == sum:
      idx1 = i
      idx2 = j
      break
value1 =sevenmini[idx1]
value2 = sevenmini[idx2]
sevenmini.remove(value1)
sevenmini.remove(value2)
for i in sevenmini:
  print(i)