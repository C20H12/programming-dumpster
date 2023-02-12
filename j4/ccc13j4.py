total = int(input())
tasks = [int(input()) for _ in range(int(input()))]
tasks.sort()

time = 0
canDo = 0
for t in tasks:
  time += t
  canDo += 1
  if time > total:
    break

print(canDo - 1)