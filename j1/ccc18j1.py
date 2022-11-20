digs = []
for i in range(4):
  digs.append(int(input()))

if (digs[0] == 8 or digs[0] == 9) and (digs[3] == 8 or digs[3] == 9) and digs[1] == digs[2] :
  print("ignore")
else:
  print("answer")

