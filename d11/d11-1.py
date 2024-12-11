def apply_rules(num):
  digits = len(str(num))
  if num == 0:
    return [1]
  elif digits%2 == 0:
    left = int(str(num)[:digits//2])
    right = int(str(num)[digits//2:])
    return [left, right]
  else:
    return [num*2024]

def get_input():
  inp = []
  with open("input", 'r') as file:
    for line in file:
      inp = list(map(int, list(line.strip().split())))
       
  return inp
  
inp = get_input()
temp = []
  
for i in range(25):
  for j in range(len(inp)):
    elem = apply_rules(inp.pop(0))
    while elem:
      temp.append(elem.pop(0))
  inp = temp
  temp = []


print(len(inp))