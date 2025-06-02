n, m = map(int, input().split())
Alist = []
Blist = []
result = []
for i in range(n):
  Alist.append(list(map(int, input().split())))
    
for i in range(n):
  Blist.append(list(map(int, input().split())))

for i in range(n):
  for j in range(m):
    result.append(Alist[i][j]+Blist[i][j])
for i in range(n * m):
  if (i+1) % m == 0:
    print(result[i])
  else :
    print(result[i], end=" ")