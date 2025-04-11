T = int(input())
sum = []

for i in range(T):
    A, B = map(int, input().split())
    result = A + B
    sum.append(result)
for i in range(T):
    print("Case #", i + 1, ": ", sum[i], sep='')
        