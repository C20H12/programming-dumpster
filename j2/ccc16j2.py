square = []

for i in range(4):
	row = [int(e) for e in input().split()]		
	square.append(row)

rowSumArr = []
colSumArr = []
for i in range(4):
	rowSum = 0
	colSum = 0
	
	for j in range(4):
		rowSum += square[i][j]
		colSum += square[j][i]
		
	colSumArr.append(colSum)
	rowSumArr.append(rowSum)

isMagic = True
prevRowSum, prevColSum = 0, 0
for i in range(4):
	if i > 0:
		if prevRowSum != rowSumArr[i] or prevColSum != colSumArr[i] or rowSumArr[i] != colSumArr[i]:
			isMagic = False
			break
	prevRowSum, prevColSum = rowSumArr[i], colSumArr[i]
	
	
print("magic" if isMagic else "not magic")
	