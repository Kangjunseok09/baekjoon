import sys
input = sys.stdin.readline
while True:
  n = int(input())
  if n == -1:
    break
  num = []
  for i in range(1,n):
    if n % i == 0:
      num.append(i)
    
  if sum(num) == n:
    print(n, " = ", " + ".join(str(i) for i in num), sep="")
  else:
    print(f"{n} is NOT perfect.")