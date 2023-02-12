import sys
input = sys.stdin.readline

n, q = list(map(int, input().split()))
ds = list(map(int, input().split()))

for j in range(q):
  mj, kj = list(map(int, input().split()))
  maxPt = 0
  for i in range(len(ds)):
    if mj ^ i <= kj:
      maxPt = max(maxPt, ds[i])
    print(mj ^ i)
  print(maxPt)