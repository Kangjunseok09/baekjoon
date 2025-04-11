n = int(input())
f = [0,1]

for i in range(n):
    f[i] = f[i-1] + f[i-2]
    f.append(f[i])

print(f[n])