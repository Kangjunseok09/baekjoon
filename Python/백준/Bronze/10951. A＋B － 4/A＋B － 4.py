result = []
while True:
    try:
        a, b = map(int, input().split())
        result.append(a+b)
    except EOFError:
        for i in range(len(result)):
            print(result[i])
        break
