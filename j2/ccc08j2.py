initList = ["A", "B", "C", "D", "E"]

def btn1(arr):
	temp = []
	for i in range(1, len(arr)):
		temp.append(arr[i])
	temp.append(arr[0])
	return temp

def btn2(arr):
	temp = [arr[len(arr) - 1]]
	for i in range(len(arr) - 1):
		temp.append(arr[i])
	return temp

def btn3(arr):
	arr[0], arr[1] = arr[1], arr[0]
	return arr

buttons = [None, btn1, btn2, btn3]

finList = initList
while True:
	b = int(input())
	n = int(input())
	
	if b == 4 and n == 1:
		print("{} {} {} {} {}".format(*finList))
		break
	
	for i in range(n):
		finList = buttons[b](finList)
		
"""
2
1
3
1
2
3
4
1
"""