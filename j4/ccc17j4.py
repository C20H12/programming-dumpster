
def isSequence(hr, mn):
  t1 = hr // 10
  t2 = hr % 10
  t3 = mn // 10
  t4 = mn % 10
  if t1 == 0:
    if t2 - t3 == t3 - t4:
      return True
  elif t1 - t2 == t2 - t3 == t3 - t4:
    return True
  return False
  

numberOfSeqs = 0
for h in range(1, 13):
  for m in range(60):
    if isSequence(h, m):
      # print(h, m)
      numberOfSeqs += 1
# print(numberOfSeqs)

inp = int(input())
count = inp // 720 * numberOfSeqs

h = 12
for m in range(1, inp % 720 + 1):
  if m % 60 == 0:
    h += 1
    h %= 12
    if h == 0:
      h = 12
  if isSequence(h, m % 60):
    # print(h, m % 60)
    count += 1

print(count)