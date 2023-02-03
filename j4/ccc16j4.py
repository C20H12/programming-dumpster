from datetime import datetime, timedelta

def pad(n):
  if n < 10:
    return "0" + str(n)
  return str(n)

h, m = [int(n) for n in input().split(':')]
time = datetime(year=1, month=1, day=1, hour=h, minute=m)
rush1 = [datetime(year=1, month=1, day=1, hour=7), datetime(year=1, month=1, day=1, hour=10)]
rush2 = [datetime(year=1, month=1, day=1, hour=15), datetime(year=1, month=1, day=1, hour=19)]


if not rush1[0] <= time <= rush1[1] and not rush2[0] <= time <= rush2[1]:
  endT = time + timedelta(hours=2)
  if not rush1[0] <= endT <= rush1[1] and not rush2[0] <= endT <= rush2[1]:
    print(f"{pad(endT.hour)}:{pad(endT.minute)}")
  else:
    if endT >= rush2[0]:
      diff = endT - rush2[0]
      res = rush2[0] + diff * 2
      print(f"{pad(res.hour)}:{pad(res.minute)}")
    else:
      diff = endT - rush1[0]
      res = rush1[0] + diff * 2
      if res > rush1[1]:
        diff = res - rush1[1]
        res = rush1[1] + diff / 2
      print(f"{pad(res.hour)}:{pad(res.minute)}")
      


if rush1[0] <= time <= rush1[1] or rush2[0] <= time <= rush2[1]:
  endT = time + timedelta(hours=4)
  if rush1[0] <= endT <= rush1[1] and rush2[1] <= endT <= rush2[1]:
    print(f"{pad(endT.hour)}:{pad(endT.minute)}")
  else:
    if endT >= rush2[1]:
      diff = endT - rush2[1]
      res = rush2[1] + diff / 2
      print(f"{pad(res.hour)}:{pad(res.minute)}")
    else:
      diff = endT - rush1[1]
      res = rush1[1] + diff / 2
      print(f"{pad(res.hour)}:{pad(res.minute)}")


