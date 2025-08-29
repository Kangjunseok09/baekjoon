
t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    last = pow(a, b, 10)   # (a^b) % 10
    if last == 0:
        print(10)
    else:
        print(last)