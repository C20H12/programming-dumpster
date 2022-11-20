from math import floor


h = int(input())
halfH = floor(h / 2)
centerLen = h * 2

for i in range(halfH):
  asterisks = 1 + i * 2
  print(asterisks * "*" + (centerLen - asterisks * 2) * " " + asterisks * "*")

print(centerLen * "*")

for i in range(halfH - 1, -1, -1):
  asterisks = 1 + i * 2
  print(asterisks * "*" + (centerLen - asterisks * 2) * " " + asterisks * "*")
