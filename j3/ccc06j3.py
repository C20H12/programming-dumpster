keyGroups = [
  "abc",
  "def",
  "ghi",
  "jkl",
  "mno",
  "pqrs",
  "tuv",
  "wxyz",
]

while True:
  word = input()

  if word == "halt":
    break
  
  count = 0
  lastGrp = ""
  for letter in word:
    for grp in keyGroups:
      if letter in grp:
        count += grp.index(letter) + 1
        if letter in lastGrp:
          count += 2
        lastGrp = grp
        break
  print(count)
