apples = []
bananas = []
for i in range(3):
  apples.append(int(input()))
for i in range(3):
  bananas.append(int(input()))

ascore = apples[0] * 3 + apples[1] * 2 + apples[2] * 1
bscore = bananas[0] * 3 + bananas[1] * 2 + bananas[2] * 1

if ascore > bscore:
  print('A')
elif bscore > ascore:
  print('B')
else:
  print('T')