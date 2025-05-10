import math
a, b = map(int, input().split())
g = math.gcd(a, b)
l = math.lcm(a, b)
print(g)
print(l)