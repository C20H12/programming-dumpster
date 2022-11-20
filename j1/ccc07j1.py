weights = []
for i in range(3):
  weights.append(int(input()))

weights.sort()
middle = weights[1]

print(middle)