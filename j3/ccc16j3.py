word = input()

def findLongestPalindrome(word):
  longestPalindrome = 0
  length = len(word)
  for i in range(length - 2, -1, -1):
    combos = []
    for j in range(length - i):
      combos.append(word[j : j+i+1])
    
    # print(combos)
    for combo in set(combos):
      if len(combo) < longestPalindrome:
        return longestPalindrome
      if combo == combo[::-1]:
        # print(combo)
        return len(combo)
        

if word == word[::-1]:
  print(len(word))
else:
  print(findLongestPalindrome(word))
