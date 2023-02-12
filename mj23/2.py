start = int(input())
end = int(input())

if (20 <= start <= 23) and (6 <= end <= 9) and (8 <= end + 24 - start <= 10):
  print("Healthy")
else:
  print("Unhealthy")
