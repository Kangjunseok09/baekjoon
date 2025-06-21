from collections import deque
n = int(input())
card = deque(range(1, n+1))
while len(card) > 1:
  card.popleft()
  back = card.popleft()
  card.append(back)
print(card[0])