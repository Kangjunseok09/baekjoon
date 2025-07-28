m, n = map(int, input().split())

isprime = [0] * (n+1)
isprime[0] = 1
isprime[1] = 1
for i in range(2, int(n**0.5)+1):
  if isprime[i] == 0:
    for j in range(i*i, n+1, i):
      isprime[j] = 1

for i in range(m, n+1):
  if not isprime[i]:
    print(i)
  
