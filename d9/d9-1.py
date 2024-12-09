import numpy as np

inp = []
with open("input", 'r') as file:
  for line in file:
    matches = list(line.strip())
    inp = list(map(int, matches))
  
diskmap = []
for i in range(len(inp)):
  if i%2==0:
    elem = i//2
  else:
    elem = None

  for j in range(inp[i]):
    diskmap.append(elem)


for i in range(len(diskmap)):
  try:
    if diskmap[i] is None:
      elem = None
      while elem == None:
        elem = diskmap.pop()
      diskmap[i] = elem
  except IndexError:
    break

output = sum(map(lambda x: x[0]*x[1], enumerate(diskmap)))
print(output)