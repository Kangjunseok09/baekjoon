n = int(input())
start = n
cur = n
cnt = 0

while True:
    a = cur // 10
    b = cur % 10
    s = a + b
    cur = (b * 10) + (s % 10)
    cnt += 1
    if cur == start:
        break

print(cnt)