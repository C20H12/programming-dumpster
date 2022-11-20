w = int(input())
h = float(input())
index = w / h ** 2

if index > 25:
  print("Overweight")
elif index >= 18.5:
  print("Normal weight")
else:
  print("Underweight")