start = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))
charge = int(input())

chargeNeeded =abs(start[0]-end[0]) + abs(start[1]-end[1])

if charge - chargeNeeded >= 0 and (charge - chargeNeeded) % 2 == 0:
  print("Y")
else:
  print("N")

# start = list(map(int, input().split()))
# end = list(map(int, input().split()))
# charge = int(input())

# charge -= abs(start[0]-end[0]) + abs(start[1]-end[1])

# if charge >=0 and charge % 2 == 0:
#   print("Y")
# else:
#   print("N")