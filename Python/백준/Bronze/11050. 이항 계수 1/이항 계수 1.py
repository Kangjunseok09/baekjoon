n, k = map(int, input().split())

def fac(a):
  fac = 1
  for i in range(1, a+1):
    fac *= i
  return fac

print(f"{fac(n) // (fac(k) * fac(n-k))}")