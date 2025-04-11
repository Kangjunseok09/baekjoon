h, w = map(int, input().split())
list = list(map(int, input().split()))
result = 0

for i in range(1, w-1):
  left = max(list[:i])
  right = max(list[i:])
  standard = min(left, right)
  if standard > list[i]:
    result += standard - list[i]
  
print(result)