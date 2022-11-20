word = input()

vowels = "aeiou"

output = ""

def getNearestVowel(letter):
  closest = "a"
  for i in range(len(vowels)):
    currentV = vowels[i]
    nextV = vowels[i+1] if i < len(vowels)-1 else vowels[0]
    closest = min(closest, currentV, nextV, key = lambda x: abs(ord(x) - ord(letter)))

  return closest

# print(getNearestVowel("n"))

for i in word:
  if i in vowels:
    output += i
  else:
    nextLetter = chr(ord(i) + 1)
    if nextLetter in vowels:
      nextLetter = chr(ord(nextLetter) + 1)
    elif i == "z":
      nextLetter = "z"

    output += i + getNearestVowel(i) + nextLetter

print(output)