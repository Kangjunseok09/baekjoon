m = int(input())
n = int(input())
prime = []
for i in range(m, n+1):
  if i < 2:
    continue
  isprime = True
  for j in range(2, int(i**0.5)+1):
    if i % j == 0:
      isprime = False
      break
  if isprime:
    prime.append(i)
  
if len(prime) == 0:
  print(-1)
else:
  print(sum(prime))
  print(prime[0])