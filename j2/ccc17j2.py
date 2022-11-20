# num = int(input())
# shift_amt = int(input())

# def shift(num, amt):
#   zeros = ''
#   for _ in range(amt):
#     zeros += '0'
#   return int(str(num) + zeros)

# total = num
# for i in range(shift_amt):
#   total += shift(num, i + 1)

# print(total)

num = int(input())
shift_amt = int(input())
total = num

for i in range(shift_amt):
  total += num * 10 ** (i + 1)

print(total)