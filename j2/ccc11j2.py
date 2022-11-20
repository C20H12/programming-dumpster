h = int(input())
m = int(input())

finishedHour = -1
for t in range(1, m+1):
	alt = -6 * t ** 4 + h * t ** 3 + 2 * t ** 2 + t

	if alt <= 0:
		finishedHour = t
		break

if finishedHour > 0:
	print("The balloon first touches ground at hour:")
	print(finishedHour)
else:
	print("The balloon does not touch ground in the given time.")