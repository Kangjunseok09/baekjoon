n = int(input())

x_coordinates = []
y_coordinates = []
for i in range(n):
  x, y = map(int, input().split())
  x_coordinates.append(x)
  y_coordinates.append(y)

print((max(x_coordinates) - min(x_coordinates)) * (max(y_coordinates) - min(y_coordinates)))
  
