# from time import time

trout, pike, pick, total = [int(input()) for _ in range(4)]
# ways = 0

# t0 = time()
# for i in range(total+1):
#   for j in range(total+1):
#     for k in range(total+1):
#       if i > 0 or j > 0 or k > 0:
#         if i*trout + j*pike + k*pick <= total:
#           print(f"{i} Brown Trout, {j} Northern Pike, {k} Yellow Pickerel")
#           ways += 1

# print(f"Number of ways to catch fish: {ways}")

# t1 = time()
# print(f"Time: t1-t0")

"""
1
2
3
2


1 Brown Trout, 0 Northern Pike, 0 Yellow Pickerel
2 Brown Trout, 0 Northern Pike, 0 Yellow Pickerel
0 Brown Trout, 1 Northern Pike, 0 Yellow Pickerel
Number of ways to catch fish: 3
"""

checked = []
combinations = []

def dfs(num, p, g, r):
  if num > total:
    return
  
  if str(p) + str(g) + str(r) in checked:
    return
  
  checked.append(str(p) + str(g) + str(r))

  if num >= 1 and num <= total: 
    combinations.append((p, g, r));

    if num == total:
      return
  
  dfs(num + trout, p + 1, g, r)
  dfs(num + pike, p, g + 1, r)
  dfs(num + pick, p, g, r + 1)

dfs(0, 0, 0, 0)
for i in combinations:
  print(f"{i[0]} Brown Trout, {i[1]} Northern Pike, {i[2]} Yellow Pickerel")

print(f"Number of ways to catch fish: {len(combinations)}")
