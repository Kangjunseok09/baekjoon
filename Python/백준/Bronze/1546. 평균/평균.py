n = int(input())
score = list(map(int, input().split()))
avg = 0
for i in range(n):
  avg += score[i]/max(score)*100

print(avg/n)

