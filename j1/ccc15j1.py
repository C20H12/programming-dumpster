mon = int(input())
day = int(input())

if mon == 2 and day == 18:
  print("Special")
elif (mon == 2 and day < 18) or mon < 2:
  print("Before")
else:
  print("After")
