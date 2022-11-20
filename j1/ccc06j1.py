burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())

burgers = {
  1: 461,
  2: 431,
  3: 420,
  4: 0
}
sides = {
  1: 100,
  2: 57,
  3: 70,
  4: 0
}
drinks = {
  1: 130,
  2: 160,
  3: 118,
  4: 0
}
desserts = {
  1: 167,
  2: 266,
  3: 75,
  4: 0
}
print(f"Your total Calorie count is {burgers[burger] + sides[side] + drinks[drink] + desserts[dessert]}.")