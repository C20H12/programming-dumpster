# ln = int(input())
# output = ""

# for i in range(ln):
#   encoded = input() + " "

#   count = 0

#   for j in range(len(encoded) - 1):
#     if encoded[j] == encoded[j+1]:
#       count += 1
#     else:
#       count += 1
#       output += str(count) + " " + encoded[j] + " "
#       count = 0
  
#   output += '\n' if i != ln - 1 else ""

# print(output)

"""
4
+++===!!!!
777777......TTTTTTTTTTTT
(AABBC)
3.1415555


3 + 3 = 4 !
6 7 6 . 12 T
1 ( 2 A 2 B 1 C 1 )
1 3 1 . 1 1 1 4 1 1 4 5
"""

def splitString(string):
  string = string + ' '
  output = []
  last = 0
  for i in range(len(string) - 1):
    if string[i] != string[i+1]:
      output.append(string[last:i+1])
      last = i+1
  return output

ln = int(input())
output = ""

for i in range(ln):
  encoded = input()
  splitted = splitString(encoded)
  for j in splitted:
    output += str(len(j)) + " " + j[0] + " "
  
  output += '\n' if i != ln - 1 else ""

print(output)