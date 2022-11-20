spots = int(input())
yesterday = list(input())
today = list(input())
both = 0

for i in range(spots):
  if yesterday[i] == today[i] == 'C':
    both += 1

print(both)