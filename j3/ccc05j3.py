turns = []
streets = []

while True:
  inst = input()

  if inst == "R" or inst == "L":
    turns.append(inst)
  elif inst == "SCHOOL":
    break
  else:
    streets.append(inst)
  
while len(turns) != 1:
  direction = "RIGHT" if turns.pop() == 'L' else "LEFT"
  print(f"Turn {direction} onto {streets.pop()} street.")

direction = "RIGHT" if turns.pop() == 'L' else "LEFT"
print(f"Turn {direction} into your HOME.")