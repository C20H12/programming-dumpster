sentence = input()
happy = 0
sad = 0

# happy = sentence.count(":-)")
# sad = sentence.count(":-(")

for i in range(1, len(sentence)):
	if sentence[i-1] == ":" and sentence[i] == "-":
		if sentence[i+1] == ")":
			happy += 1
		elif sentence[i+1] == "(":
			sad += 1

if happy == 0 and sad == 0:
	print("none")
elif happy == sad:
	print("unsure")
elif happy - sad > 0:
	print("happy")
elif sad - happy > 0:
	print("sad")


#sentence = re.sub(r":-\)", 1, sentence)
#sentence = re.sub(r":-\(", -1, sentence)
#print(list(sentence))
