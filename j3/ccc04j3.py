nouns = int(input())
adjs = int(input())

nounsArr = []
adjsArr = []

for i in range(nouns):
  nounsArr.append(input())

for i in range(adjs):
  adjsArr.append(input())

for i in nounsArr:
  for j in adjsArr:
    print(f"{i} as {j}")
