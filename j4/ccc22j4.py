# yesGroupsN = int(input())
# yesGroups = {}
# for i in range(yesGroupsN):
#   name1, name2 = input().split()
#   if name1 in yesGroups:
#     yesGroups[name1].append(name2)
#   else:
#     yesGroups[name1] = [name2]
#   if name2 in yesGroups:
#     yesGroups[name2].append(name1)
#   else:
#     yesGroups[name2] = [name1]

# noGroupsN = int(input())
# noGroups = {}
# for i in range(noGroupsN):
#   name1, name2 = input().split()
#   if name1 in noGroups:
#     noGroups[name1].append(name2)
#   else:
#     noGroups[name1] = [name2]
#   if name2 in noGroups:
#     noGroups[name2].append(name1)
#   else:
#     noGroups[name2] = [name1]


yesGroupsN = int(input())
yesGroups = []
for i in range(yesGroupsN):
  name1, name2 = input().split()
  yesGroups.append((name1, name2))

noGroupsN = int(input())
noGroups = []
for i in range(noGroupsN):
  name1, name2 = input().split()
  noGroups.append((name1, name2))



groupsN = int(input())
groups = {}

for i in range(groupsN):
  name1, name2, name3 = input().split()
  groups[name1] = (name2, name3)
  groups[name2] = (name1, name3)
  groups[name3] = (name1, name2)

violateCount = 0

for name1, name2 in yesGroups:
  if name1 in groups and name2 in groups:
    groupName1, groupName2 = groups[name1][0], groups[name1][1]
    if name2 != groupName1 and name2 != groupName2:
      violateCount += 1
for name1, name2 in noGroups:
  if name1 in groups and name2 in groups:
    groupName1, groupName2 = groups[name1][0], groups[name1][1]
    if name2 == groupName1 or name2 == groupName2:
      violateCount += 1

print(violateCount)


# for k in groups:
#   if k in yesGroups and yesGroups[k]:
#     if groups[k][0] not in yesGroups[k] and groups[k][1] not in yesGroups[k]:
#       violateCount += 1
#       for i in range(len(yesGroups[k])):
#         del yesGroups[yesGroups[k][i]]
#   if k in noGroups and noGroups[k]:
#     if groups[k][0] in noGroups[k] or groups[k][1] in noGroups[k]:
#       violateCount += 1
#       for i in range(len(noGroups[k])):
#         del noGroups[noGroups[k][i]]
  

# print(len(yesGroups.keys()))
  # names = input().split()
  
  # for name in names:
  #   if name in yesGroups:
  #     shouldBeWith = yesGroups[name]
  #     for shouldName in shouldBeWith:
  #       if shouldName not in names:
  #         violateCount += 1
  #         try:
  #           del yesGroups[name], yesGroups[shouldName]
  #         except:
  #           pass
  #         break
  #   if name in noGroups:
  #     shouldNotBeWith = noGroups[name]
  #     for shouldName in shouldNotBeWith:
  #       if shouldName in names:
  #         violateCount += 1
  #         try:
  #           del noGroups[name], noGroups[shouldName]
  #         except:
  #           pass
  #         break

  # name1, name2, name3 = input().split()
  # validYes, validNo = True, True
  # if name1 in yesGroups and name2 in yesGroups:
  #   if name2 not in yesGroups[name1] or name1 not in yesGroups[name2]:
  #     validYes = False
  # if name1 in noGroups and name2 in noGroups:
  #   if name2 in noGroups[name1] or name1 in noGroups[name2]:
  #     validNo = False
  
  # if name1 in yesGroups and name3 in yesGroups:
  #   if name3 not in yesGroups[name1] or name1 not in yesGroups[name3]:
  #     validYes = False
  # if name1 in noGroups and name3 in noGroups:
  #   if name3 in noGroups[name1] or name1 in noGroups[name3]:
  #     validNo = False
  
  # if name2 in yesGroups and name3 in yesGroups:
  #   if name3 not in yesGroups[name2] or name2 not in yesGroups[name3]:
  #     validYes = False
  # if name2 in noGroups and name3 in noGroups:
  #   if name3 in noGroups[name2] or name2 in noGroups[name3]:
  #     validNo = False

  # if not validYes:
  #   violateCount += 1
  # if not validNo:
  #   violateCount += 1


# print(violateCount)