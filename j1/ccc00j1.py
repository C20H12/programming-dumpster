startDay, total = input().split()
startDay = int(startDay)
total = int(total)

print("Sun Mon Tue Wed Thr Fri Sat")

for i in range(startDay - 1):
  print("    ", end="")

for i in range(1, total + 1):
  print(" " * (3 - len(str(i))) + str(i), end="")
  currentDay = (i + startDay - 1) % 7
  if currentDay == 0:
    print()
  elif i == total:
    print()
  else:
    print(" ", end="")

'''
Sun Mon Tue Wed Thr Fri Sat
          1   2   3   4   5
  6   7   8   9  10  11  12
 13  14  15  16  17  18  19
 20  21  22  23  24  25  26
 27  28  29  30
'''