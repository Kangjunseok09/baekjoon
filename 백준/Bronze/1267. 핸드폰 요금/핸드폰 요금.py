n = int(input())
fee = list(map(int, input().split()))
ysum = 0
msum = 0
for i in range(n):
  ysum += ((fee[i] // 30) + 1) * 10
  msum += ((fee[i] // 60) + 1) * 15

if ysum > msum:
  print(f"M {msum}")
elif msum > ysum:
  print(f"Y {ysum}")
else:
  print(f"Y M {ysum}")