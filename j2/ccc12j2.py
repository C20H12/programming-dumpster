prevNum = 0
rises = 0
decents = 0
consts = 0
for i in range(4):
	curr = int(input())
	
	if i > 0:	
		if curr == prevNum:
			consts += 1
		elif curr - prevNum > 0:
			rises += 1
		elif curr - prevNum < 0:
			decents += 1
		
	prevNum = curr

if rises == 3:
	print("Fish Rising")
elif decents == 3:
	print("Fish Diving")
elif consts == 3:
	print("Fish At Constant Depth")
else:
	print("No Fish")
	
