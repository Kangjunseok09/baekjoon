from collections import Counter

n, m = map(int, input().split())
arr = []
for i in range(n):
  arr.append(input())
for i in range(m):
  arr.append(input())

counter = Counter(arr)
result = [i for i in arr if counter[i] > 1]
result = list(set(result))
result.sort()
print(len(result))
for i in result:
  print(i)
