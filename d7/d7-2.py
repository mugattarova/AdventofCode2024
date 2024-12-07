import re
from itertools import product

def evallefttoright(row, perm):
  r = row.copy()
  for p in perm:
    if p == '+':
      res = r[0]+r[1]
      del r[0:2]
      r.insert(0, res)
    elif p == '*':
      res = r[0]*r[1]
      del r[0:2]
      r.insert(0, res)
    elif p == '||':
      res = int(str(r[0])+str(r[1]))
      del r[0:2]
      r.insert(0, res)
  return r[0]

def solveEq(row):
  r = row.copy()
  res = r.pop(0)
  perms = [p for p in product(['*', '+', '||'], repeat=len(r)-1)]
  for p in perms:
    if evallefttoright(r, p)==res:
      return True
  return False


inp = []
with open("input", 'r') as file:
  for line in file:
    matches = re.findall("[0-9]+", line.strip())    
    inp.append(list(map(int, matches)))
  

output = 0
for row in inp:
  if solveEq(row):
    output += row[0]

print(output)