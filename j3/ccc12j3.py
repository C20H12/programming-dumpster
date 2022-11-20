icon = [
"*x*",
" xx",
"* *"
]

scale = int(input())

for line in icon:
  scaledLine = ""
  for i in line:
    scaledLine += i * scale
  
  for i in range(scale):
    print(scaledLine)