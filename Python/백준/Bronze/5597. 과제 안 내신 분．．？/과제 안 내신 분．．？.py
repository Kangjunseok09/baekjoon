import sys
input = sys.stdin.readline
attend = []
result = []
for i in range(28):
  n = int(input())
  attend.append(n)

for i in range(1, 31):
  if not i in attend:
    result.append(i)
attend = sorted(attend)
for i in result:
  print(i)