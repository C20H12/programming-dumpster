from re import sub


while True:
	word = input()
	
	if word == "quit!":
		break
	
	if word.endswith("or") and len(word) > 4 and not word[len(word)-3] in ['a', 'e', 'i', 'o', 'u', 'y']:
		replaced = sub(r"or$", "our", word)
		print(replaced)
	else:
		print(word)
