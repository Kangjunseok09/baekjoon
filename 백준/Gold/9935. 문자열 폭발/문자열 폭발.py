s = input()
word = input()

stack = []
length = len(word)
last = word[-1]
for ch in s:
  stack.append(ch)

  if len(stack) >= length:
    if stack[-length:] == list(word): 
      for i in range(length):
        stack.pop()

if stack:
  print("".join(stack))
else:
  print("FRULA")