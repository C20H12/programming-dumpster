wins = 0
for i in range(6):
  line = input()
  if line == 'W':
    wins += 1

if wins >= 5:
  print(1)
elif wins >= 3:
  print(2)
elif wins >= 1:
  print(3)
else:
  print(-1)
 