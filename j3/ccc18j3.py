dist = list(map(int, input().split()))
output = []

for i in range(5):
  row = list(range(5))
  row[i] = 0

  for j in range(i+1, 5):
    row[j] = sum(dist[i:j])
  
  for k in range(i-1, -1, -1):
    row[k] = sum(dist[k:i])
  
  print("{} {} {} {} {}".format(*row))