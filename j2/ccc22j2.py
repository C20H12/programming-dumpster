players = int(input())
gold = 0
for i in range(players):
  p = int(input())
  f = int(input())
  if p * 5 - f * 3 > 40:
    gold += 1

print(str(gold) + '+') if gold == players else print(gold)