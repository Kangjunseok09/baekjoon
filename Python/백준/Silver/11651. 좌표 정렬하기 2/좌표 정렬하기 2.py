import sys
n = int(input())
coordinates = []
for i in range(n):
  x, y = map(int, input().split())
  coordinates.append((y, x))
coordinates = sorted(coordinates)
for i, j in coordinates:
  print(j, i)
