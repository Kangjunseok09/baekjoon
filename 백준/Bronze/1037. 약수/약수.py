n = int(input())                # 약수의 개수
divisors = list(map(int, input().split()))
print(min(divisors) * max(divisors))