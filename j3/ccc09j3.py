time = int(input())

otherTimes = [
  time - 300,
  time - 200,
  time - 100,
  time,
  time + 100,
  time + 130,
]

for i in range(6):
  if otherTimes[i] > 2359:
    otherTimes[i] -= 2400
  elif otherTimes[i] < 0:
    otherTimes[i] += 2400
  elif otherTimes[i] % 100 > 59:
    otherTimes[i] += 40
  

print(
"""{} in Ottawa
{} in Victoria
{} in Edmonton
{} in Winnipeg
{} in Toronto
{} in Halifax
{} in St. John's""".format(time, *otherTimes)
)