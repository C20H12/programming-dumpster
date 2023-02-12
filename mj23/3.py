import sys
input = sys.stdin.readline


n, k, m = input().split()
k = int(k)
m = int(m)
a = input().split()
b = input().split()

aDict = {}
i = 0
for n in a:
  aDict[int(n)] = i
  i += 1

count = 0
for i in range(len(b)):
  bi = int(b[i])
  diff = m - bi
  # print(bi, diff, abs(i - aDict[diff]))
  if diff in aDict and abs(i - aDict[diff]) >= k:
    count += 1

print(count)