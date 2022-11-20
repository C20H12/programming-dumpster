x, m = [int(input()) for _ in range(2)]

exists = True
for n in range(100):
	if x * n % m == 1:
		print(n)
		exists = True
		break
	exists = False

if not exists:
	print("No such integer exists.")


# try:
# 	y = pow(int(input()), -1, int(input()))
# 	print(y)
# except ValueError:
# 	print("No such integer exists.")