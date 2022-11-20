eliminated = int(input())

boxes = [0, 100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]

for i in range(eliminated):
  boxNum = int(input())
  boxes[boxNum] = 0

boxesSum = sum(boxes)
boxesLen = 0
for i in boxes:
  if i != 0:
    boxesLen += 1
boxesAvg = boxesSum / boxesLen

offer = int(input())

if offer > boxesAvg:
  print("deal")
else:
  print("no deal")
