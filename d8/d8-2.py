import re
from itertools import combinations
from collections import defaultdict

def findANforPair(pair):
  i1, j1 = pair[0]
  i2, j2 = pair[1]
  ans = []
  stop = False
  ishift = abs(i1-i2)
  jshift = abs(j1-j2)
  imin = min(i1, i2)
  imax = max(i1, i2)
  jmin = min(j1, j2)
  jmax = max(j1, j2)
  if float(j1-j2)/float(i1-i2) > 0:
    # decreasing antinodes
    n = 1
    while not stop:
      i = imin - n*ishift
      j = jmin - n*jshift
      if 0 <= i < len(inp) and 0 <= j < len(inp[0]):
        ans.append((i, j))
      else:
        stop = True
      n += 1
    stop = False
    # increasing antinodes
    n = 1
    while not stop:
      i = imax + n*ishift
      j = jmax + n*jshift
      if 0 <= i < len(inp) and 0 <= j < len(inp[0]):
        ans.append((i, j))
      else:
        stop = True
      n += 1
  else:    
    # decreasing antinodes
    n = 1
    while not stop:
      i = imin - n*ishift
      j = jmax + n*jshift
      if 0 <= i < len(inp) and 0 <= j < len(inp[0]):
        ans.append((i, j))
      else:
        stop = True
      n += 1
    stop = False
    # increasing antinodes
    n = 1
    while not stop:
      i = imax + n*ishift
      j = jmin - n*jshift
      if 0 <= i < len(inp) and 0 <= j < len(inp[0]):
        ans.append((i, j))
      else:
        stop = True
      n += 1

  return ans

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


output = 0
for key, arr in frequencies.items():
  if len(arr) > 2:
    for i, j in arr:
      inp[i][j] = "#"
  nodepairs = list(combinations(arr, 2))
  for pair in nodepairs:
    ans = findANforPair(pair)
    for i, j in ans:
      inp[i][j] = "#"


for l in inp:
  output += l.count('#')

print(output)