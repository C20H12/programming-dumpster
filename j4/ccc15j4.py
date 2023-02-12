lns = int(input())

friends = {}
friendTimes = {}
time = 0
for i in range(lns):
  line = input().split()
  op, n = line[0], int(line[1])
  if op == "R":
    friends[n] = {'t': time, 'replied': False}
    time += 1
  elif op == "W":
    time += n - 1
  elif op == "S":
    if n in friendTimes:
      friendTimes[n] += time - friends[n]['t']
    else:
      friendTimes[n] = time - friends[n]['t']
    friends[n]['replied'] = True
    time += 1

# print(friends)
# print(friendTimes)

for k, v in sorted(friends.items()):
  outn = -1
  if v['replied'] and k in friendTimes:
    outn = friendTimes[k]
  print(f"{k} {outn}")
