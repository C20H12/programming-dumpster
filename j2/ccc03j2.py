from math import floor, ceil


while True:
	number = int(input())
	
	if number == 0:
		break
	
	divisers = []
	for i in range(1, number+1):
		if number % i == 0:
			divisers.append(i)
	
	dimentions = [0, 0]
	length = len(divisers) - 1
	
	dimentions[0], dimentions[1] = divisers[floor(length / 2)], divisers[ceil(length / 2)]
	
	print(f"Minimum perimeter is {2 * (dimentions[0] + dimentions[1])} with dimensions {dimentions[0]} x {dimentions[1]}")