n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
  if a[i] <= 1:
    continue
  is_prime = True
  for j in range(2, int(a[i]**0.5) + 1):
    if a[i] % j == 0:
      is_prime = False
      break
  if is_prime == True :
    cnt += 1
print(cnt)