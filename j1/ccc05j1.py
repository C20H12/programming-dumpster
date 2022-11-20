day = int(input())
eve = int(input())
wek = int(input())

costADay = (day - 100) * 25 > 0 and (day - 100) * 25 or 0
costBDay = (day - 250) * 45 > 0 and (day - 250) * 45 or 0 

costA = round((costADay + eve * 15 + wek * 20) / 100, 2)
costB = round((costBDay + eve * 35 + wek * 25) / 100, 2)

print("Plan A costs " + str(costA))
print("Plan B costs " + str(costB))

if costA < costB:
  print("Plan A is cheapest.")
elif costA > costB:
  print("Plan B is cheapest.")
else:
  print("Plan A and B are the same price.")
