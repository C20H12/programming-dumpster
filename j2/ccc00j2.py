allowed = ['1', '8', '0', '6', '9']

def canRotate(digs):
  digs = str(digs)
  length = len(digs)

  for i in range(length):
    if digs[i] not in allowed:
      return False
  
  rotated = ""
  for i in range(length):
    if digs[i] == '6':
      rotated += '9'
    elif digs[i] == '9':
      rotated += '6'
    else:
      rotated += digs[i]

  return digs == rotated[::-1]


# print(canRotate(9886))
count = 0
for i in range(int(input()), int(input())+1):
  if canRotate(i):
    count += 1
    # print(i)

print(count)



# def canRotate(digs):
#   digs = str(digs)
#   length = len(digs)

#   if digs == digs[::-1]:
#     for i in range(length):
#       if digs[i] not in allowed:
#         return False
#   elif len(digs[:length//2]) == len(digs[ceil(length/2):]):

#     if not length % 2 == 0 and not digs[length//2] in allowed:
#       return False
    
#     import re
#     if not (re.search(r"^[6]+$", digs[:length//2]) and re.search(r"^[9]+$", digs[ceil(length/2):]) or \
#        re.search(r"^[9]+$", digs[:length//2]) and re.search(r"^[6]+$", digs[ceil(length/2):])):
#       return False

#   return True

# 1
# 8
# 11
# 69
# 88
# 96
# 101
# 111
# 181
# 609
# 619
# 689
# 808
# 818
# 888
# 906
# 916
# 986
# 1001
# 1111
# 1691
# 1881
# 1961
# 6009
# 6119
# 6699
# 6889
# 6969
# 8008
# 8118
# 8698
# 8888
# 8968
# 9006
# 9116
# 9696
# 9886
# 9966

# 1
# 8
# 11
# 69
# 88
# 96
# 101
# 111
# 181
# 609
# 619
# 689
# 808
# 818
# 888
# 906
# 916
# 986
# 1001
# 1111
# 1881
# 6699
# 8008
# 8118
# 8888
# 9966
low = int(input())
high = int(input())

#1 and 8 stay the same, we flip the 9 and the 6
counter = 0

for x in range(low, high+1):
  skip = False
  number = str(x)
  rotated = ""
  
  for y in range(len(number)):
    if number[y] == "6":
      rotated += "9"
    elif number[y] == "9":
      rotated += "6"
    elif number[y] == "8":
      rotated += "8"
    elif number[y] == "1":
      rotated += "1"
    elif number[y] == "0":
      rotated += "0"
    else:
      skip = True
      break
  
  if number == rotated[::-1] and skip == False:
    counter = counter + 1
    print(number)
    
print (counter)