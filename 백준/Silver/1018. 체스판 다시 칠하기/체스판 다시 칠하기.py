n, m = map(int, input().split())
chess = [list(input().strip()) for _ in range(n)]

min_paint = 64 
for i in range(n - 7):
    for j in range(m - 7):
        w_start = 0  
        b_start = 0  
        for x in range(8):
            for y in range(8):
                current = chess[i + x][j + y]
                if (x + y) % 2 == 0:
                    if current != 'W':
                        w_start += 1
                    if current != 'B':
                        b_start += 1
                else:
                    if current != 'B':
                        w_start += 1
                    if current != 'W':
                        b_start += 1
        min_paint = min(min_paint, w_start, b_start)
print(min_paint)