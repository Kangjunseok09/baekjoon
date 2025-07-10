k, n = map(int, input().split())
list = []
for i in range(k):
  list.append(int(input()))

  start = 1
  end = list[0]
while start <= end:
  lanline = 0
  mid = (start + end) // 2
  for i in range(k):
    lanline += list[i] // mid 
  if lanline >= n:
    start = mid + 1
  else:
    end = mid-1

print(end)