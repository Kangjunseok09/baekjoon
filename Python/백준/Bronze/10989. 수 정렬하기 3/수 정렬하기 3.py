import sys
input = sys.stdin.readline

count = [0] * 10001 
n = int(input())
for i in range(n):
  a = int(input())
  count[a] += 1

for i in range(1, 10001):
  if count[i] > 0:
    for j in range(count[i]):
      sys.stdout.write(f"{i}\n")