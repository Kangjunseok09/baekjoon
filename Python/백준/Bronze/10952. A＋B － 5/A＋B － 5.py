result = []

while True:
        a, b = map(int, input().split())
        if a == 0 & b == 0:
            break
        result.append(a+b)

for i in range(len(result)):
    print(result[i])