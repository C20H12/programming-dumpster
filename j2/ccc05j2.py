start = int(input())
to = int(input())
count = 0
for i in range(start, to+1):
	divisers = 0
	for j in range(1, to+1):
		if i % j == 0:
			divisers += 1
	
	if divisers == 4:
		count += 1

print(f"The number of RSA numbers between {start} and {to} is {count}")
