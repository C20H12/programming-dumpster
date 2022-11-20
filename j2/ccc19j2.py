ln = int(input())
output = ""
for i in range(ln):
  amount, char = input().split()
  for j in range(int(amount)):
    output += char
  output += '\n' if i != ln - 1 else ""

print(output)