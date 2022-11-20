treats = []
for i in range(3):
  treats.append(int(input()))

score = 0
for i in range(3):
  score += treats[i] * (i + 1)

if score >= 10:
  print("happy")
else:
  print("sad")