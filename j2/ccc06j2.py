dice1 = int(input())
dice2 = int(input())

actualSides1 = dice1 > 10 and 10 or dice1
actualSides2 = dice2 > 10 and 10 or dice2

count = 0
for i in range(1, actualSides1+1):
	for j in range(1, actualSides2+1):
		if i + j == 10:
			count += 1

_is = count == 1 and "is" or "are"
way = count == 1 and "way" or "ways"

print(f"There {_is} {count} {way} to get the sum 10.")
