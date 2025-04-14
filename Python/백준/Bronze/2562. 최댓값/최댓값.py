find_max = []
for i in range(9):
  A = int(input())
  find_max.append(A)
length = int(len(find_max))
for i in range(length):
  if find_max[i] == max(find_max):
    print(find_max[i])
    print(i+1)


