start1 = int(input())
start2 = int(input())

sequence = [start1, start2]

while True:
  length = len(sequence)
  nextNum = sequence[length - 2] - sequence[length - 1]
  if nextNum > sequence[length - 1]:
    break
  sequence.append(nextNum)

print(len(sequence) + 1)