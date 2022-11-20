pointsCount = int(input())
points = []
for i in range(pointsCount):
  points.append(tuple(map(int, input().split(","))))

largestX = max([point[0] for point in points])
largestY = max([point[1] for point in points])
smallestX = min([point[0] for point in points])
smallestY = min([point[1] for point in points])

print(f"{smallestX-1},{smallestY-1}")
print(f"{largestX+1},{largestY+1}")