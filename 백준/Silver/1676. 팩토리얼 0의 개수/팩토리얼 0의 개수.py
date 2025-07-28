n = int(input())
fac = 1
a = 10
cnt = 0
for i in range(1, n+1):
  fac *= i
while True:
  if fac % a == 0 :
    cnt += 1
  else :
    break
  a *= 10
print(cnt)