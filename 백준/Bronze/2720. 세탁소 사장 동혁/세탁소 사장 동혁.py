import sys
input = sys.stdin.readline

money = [25, 10, 5, 1]
n = int(input())
list = [int(input()) for i in range(n)]

for i in list:
  for j in money:
    print(i // j, end=" ")
    i %= j
  print()