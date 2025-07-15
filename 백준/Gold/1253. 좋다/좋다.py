n = int(input())

a = list(map(int, input().split()))
a.sort()
good = 0

for i in range(n):
  number = a[i]
  start = 0
  end = n-1
  while start < end:
    if start == i:
      start += 1
      continue
    if end == i:
      end -= 1
      continue
    if a[start] + a[end] == number:
      good += 1
      break
    elif a[start] + a[end] < number:
      start += 1
    else:
      end -= 1

print(good)