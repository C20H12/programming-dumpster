p = int(input())
firstDay = int(input())
rate = int(input())

currentNumber = firstDay
lastNumber = firstDay
day = 0
while currentNumber <= p:
  currentNumber += lastNumber * rate
  lastNumber *= rate
  day += 1

print(day)