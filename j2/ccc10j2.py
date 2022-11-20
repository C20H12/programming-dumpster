nik = (int(input()), int(input()))
bry = (int(input()), int(input()))
steps = int(input())

nikSteps,brySteps,nikAbsSteps,bryAbsSteps = 0,0,0,0

for i in range(1, steps+1):
  if i % 2 == 0:
    nikSteps -= nik[1]
    nikAbsSteps += nik[1]
  else:
    nikSteps += nik[0]
    nikAbsSteps += nik[0]
  
  # nikSteps += i % 2 == 0 and -nik[1] or nik[0]
  
  if nikAbsSteps >= steps:
    if nikAbsSteps > steps:
      nikSteps -= nikAbsSteps - steps
    break

for i in range(1, steps+1):
  if i % 2 == 0:
    brySteps -= bry[1]
    bryAbsSteps += bry[1]
  else:
    brySteps += bry[0]
    bryAbsSteps += bry[0]
  
  if bryAbsSteps >= steps:
    if bryAbsSteps > steps:
      brySteps -= bryAbsSteps - steps
    break


if nikSteps > brySteps:
  print("Nikky")
elif brySteps > nikSteps:
  print("Byron")
else:
  print("Tied")
