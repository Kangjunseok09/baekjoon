H, M = map(int, input().split())
0 <= H < 24
0 <= M < 60
M = M -45
if M < 0 :
    H -= 1
    M = 60 + M
if H < 0 :
    H += 24
print(H, M)

