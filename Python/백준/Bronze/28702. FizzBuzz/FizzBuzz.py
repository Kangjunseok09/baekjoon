import random
f = input()
s = input()
t = input()

if f.isdigit():
  i = int(f) + 3
elif s.isdigit():
  i = int(s) + 2
elif t.isdigit():
  i = int(t) + 1



if i%3 == 0 and i % 5 == 0:
  print("FizzBuzz")
elif i % 3 == 0:
  print("Fizz")
elif i % 5 == 0:
  print("Buzz")
else:
  print(i)
