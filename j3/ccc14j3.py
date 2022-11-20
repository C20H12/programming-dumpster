rounds = int(input())

aPoints =  100
bPoints =  100

for i in range(rounds):
  aRoll, bRoll = tuple(map(int, input().split()))
  if aRoll > bRoll:
    bPoints -= aRoll
  elif aRoll < bRoll:
    aPoints -= bRoll

print(aPoints)
print(bPoints)
