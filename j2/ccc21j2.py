bids = int(input())
highest = 0
highest_name = ''

for i in range(bids):
  name = input()
  amount = int(input())
  if amount > highest:
    highest = amount
    highest_name = name

print(highest_name)