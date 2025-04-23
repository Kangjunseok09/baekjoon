n = int(input())
a = list(map(int, input().split()))
T, P = map(int, input().split())
result = 0
resultp = 0
for i in range(6):
  if a[i] % T > 0 :
    result += a[i] // T + 1
  else:
    result += a[i] //T

print(result)
print(n // P, n % P)
