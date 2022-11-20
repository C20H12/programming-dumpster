variables = {
  'A' : 0,
  'B' : 0,
}

def cmd1(var, val):
  variables[var] = int(val)

def cmd3(var1, var2):
  variables[var1] += variables[var2]

def cmd4(var1, var2):
  variables[var1] *= variables[var2]

def cmd5(var1, var2):
  variables[var1] -= variables[var2]

def cmd6(var1, var2):
  variables[var1] //= variables[var2]

commands = {
  '1' : cmd1,
  '3' : cmd3,
  '4' : cmd4,
  '5' : cmd5,
  '6' : cmd6,
}


while True:
  cmd = input()

  if cmd == '7':
    break
  
  cmd = cmd.split()

  if cmd[0] == '2':
    print(variables[cmd[1]])
    continue

  commands[cmd[0]](cmd[1], cmd[2])
