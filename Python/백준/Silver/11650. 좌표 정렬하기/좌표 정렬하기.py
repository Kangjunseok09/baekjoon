import sys
input = sys.stdin.readline
coordinates = []
n = int(input())
for i in range(n):
  x, y = map(int, input().split())
  coordinates.append((x, y))

coordinates = sorted(coordinates)
for f, s in coordinates:
  print(f, s)
