n = int(input())
a = 666
cnt = 0
while True:
  a = str(a)
  if a.count('666'):
    cnt += 1
  if cnt == n:
    print(a)
    break
  a = int(a)
  a += 1