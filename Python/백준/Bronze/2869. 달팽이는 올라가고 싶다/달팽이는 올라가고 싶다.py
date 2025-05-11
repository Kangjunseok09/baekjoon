import math
a, b, v = map(int, input().split())
result =math.ceil((v - a) / (a-b)) + 1
print(int(result))