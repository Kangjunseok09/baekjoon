n = int(input())

sum = 2
fib = [1, 1]
for i in range(3, n+1):
    if i % 2 == 1:
        fib[0] = fib[0] + fib[1]
        sum += fib[0]
    else:
        fib[1] = fib[1] + fib[0]
        sum += fib[1]
if n == 1:
    sum = fib[0]
elif n == 2:
    sum = fib[0] + fib[1]

print(sum * 2 + 2)

