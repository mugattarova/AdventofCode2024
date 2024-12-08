import re
from itertools import combinations
from collections import defaultdict

def findANforPair(pair):
  i1, j1 = pair[0]
  i2, j2 = pair[1]
  if float(j1-j2)/float(i1-i2) > 0:
    return [(min(i1, i2) - abs(i1-i2), min(j1, j2) - abs(j1-j2)), (max(i1, i2) + abs(i1-i2), max(j1, j2) + abs(j1-j2))]
  else:
    return[(min(i1, i2) - abs(i1-i2), max(j1, j2) + abs(j1-j2)), (max(i1, i2) + abs(i1-i2), min(j1, j2) - abs(j1-j2))]


inp = []
with open("input", 'r') as file:
  for line in file:
    matches = list(line.strip())
    inp.append(matches)
  
frequencies = defaultdict(list)

for i in range(len(inp)):
  for j in range(len(inp[0])):
    if inp[i][j] != ".":
      frequencies[inp[i][j]].append((i, j))


for key, arr in frequencies.items():
  nodepairs = list(combinations(arr, 2))
  for pair in nodepairs:
    ans = findANforPair(pair)
    for x, y in ans:
      if 0 <= x < len(inp) and 0 <= y < len(inp[0]):
        inp[x][y] = "#"



output = 0
for l in inp:
  output += l.count('#')
  print(str(l))

print(output)