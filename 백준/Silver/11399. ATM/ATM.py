n = int(input())
alist = list(map(int, input().split()))
result = 0
befo = 0
for i in range(n):
  idx = alist.index(min(alist))
  befo += alist.pop(idx)
  result += befo
print(result)
  
