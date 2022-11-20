allKeys = [
  ['A','B','C','D','E','F'],
  ['G','H','I','J','K','L'],
  ['M','N','O','P','Q','R'],
  ['S','T','U','V','W','X'],
  ['Y','Z',' ','-','.','e']
]
keyLocations = {}

for i in range(len(allKeys)):
  for j in range(len(allKeys[i])):
    keyLocations[allKeys[i][j]] = (i,j)

msg = input() + "e"

prevCoords = (0,0)
moveCount = 0
for i in msg:
  xDiff = abs(keyLocations[i][0] - prevCoords[0])
  yDiff = abs(keyLocations[i][1] - prevCoords[1])
  moveCount += xDiff + yDiff
  prevCoords = keyLocations[i]

print(moveCount)