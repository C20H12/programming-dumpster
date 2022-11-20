num = int(input())
count = 0
memo = []

for i in range(9):
  if num - i in memo:
    break
  if num - i > 5:
    continue
  count += 1
  memo.append(i)
  

print(count)