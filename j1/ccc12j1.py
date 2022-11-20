limit = int(input())
speed = int(input())

if speed <= limit:
  print("Congratulations, you are within the speed limit!")
else:
  over = speed - limit
  fine = 0
  if over >= 31:
    fine = 500
  elif over >= 21:
    fine = 270
  else:
    fine = 100
  print("You are speeding and your fine is ${}.".format(fine))

