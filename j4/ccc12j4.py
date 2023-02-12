k = int(input())
word = input()
newWord = ''

for i in range(1, len(word) + 1):
  letter = ord(word[i - 1]) - 65
  shiftAmt = 3 * i + k
  shifted = (letter - shiftAmt) % 26 + 65
  newWord += chr(shifted)

print(newWord)

# newWord = [chr(((ord(word[i - 1]) - 65) - (3 * i + k)) % 26 + 65) for i in range(1, len(word) + 1)]
# print(''.join(newWord))