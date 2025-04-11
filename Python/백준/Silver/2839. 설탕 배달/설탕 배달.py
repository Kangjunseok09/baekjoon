n= int(input())

s_count=0


while n >= 0:
    if n % 5== 0:
        s_count += n // 5
        n %= 5
        break

    n -= 3
    s_count += 1

    if n < 0:
        s_count=-1
        break

print(s_count)