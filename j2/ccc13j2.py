allowed_chars = ["I", "O", "S", "H", "Z", "X", "N"]

word = input()

valid = True
for letter in word:
	if not letter in allowed_chars:
		valid = False
		break

print("YES" if valid else "NO")
