import sys
input = sys.stdin.readline
T = int(input())
result = []
for i in range(T):
  a, b = map(int, input().split())
  result.append(a+b)
for i in result:
  print(i)