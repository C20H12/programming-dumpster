last = ""
while True:
  inst = input()

  if inst == "99999":
    break

  output = ""
  dig1 = int(inst[0])
  dig2 = int(inst[1])
  if dig1 + dig2 == 0:
    output += last
  elif (dig1 + dig2) % 2 == 0:
    output += "right "
    last = "right "
  else:
    output += "left "
    last = "left "
  
  for i in range(2, 5):
    output += inst[i]
  
  print(output)
