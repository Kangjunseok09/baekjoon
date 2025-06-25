import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
card = list(map(int, input().split()))
card_counter = Counter(card)
m = int(input())
have = list(map(int, input().split()))

for i in range(m):
  print(card_counter[have[i]], end=" ")