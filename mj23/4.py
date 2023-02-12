import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

origPts = 0
for l in s:
  if l != '*':
    origPts += ord(l) - 96

stars = s.count('*')
sl = [1] * stars

def pt() :
  idx = 0
  for l in s:
    if l == '*':
      print(chr(sl[idx] + 96), end='')
      idx += 1
    else:
      print(l, end='')
  print()

n2 = stars + origPts
if n2 < n and stars >= 1:
  if n - n2 < 26:
    sl[-1] += n - n2
    pt()
  else:
    df = n - n2
    spots = df // 25
    left = df % 25
    if spots <= len(sl):
      for i in range(1, spots + 1):
        sl[-i] += 25
      try:
        sl[-i-1] = left + 1
        pt()
      except:
        pt()
    else:
      print("Impossible")
elif n2 == n:
  pt()
else:
  print("Impossible")
