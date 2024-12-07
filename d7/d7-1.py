import re
from itertools import product

def evalExpression(row, perm):
  r = row.copy()
  for i in range(len(perm)):
    r.insert(i*2+1, perm[i])
  while '*' in r:
    ind = r.index('*')
    res = r[ind-1]*r[ind+1]
    del r[ind-1:ind+2]
    r.insert(ind-1, res)
  while '+' in r:
    ind = r.index('+')
    res = r[ind-1]+r[ind+1]
    del r[ind-1:ind+2]
    r.insert(ind-1, res)
  return r[0]

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
  return r[0]

def solveEq(row):
  r = row.copy()
  res = r.pop(0)
  perms = [p for p in product(['*', '+'], repeat=len(r)-1)]
  for p in perms:
    if evallefttoright(r, p)==res:
      return True
  return False


inp = []
with open("test", 'r') as file:
  for line in file:
    matches = re.findall("[0-9]+", line.strip())    
    inp.append(list(map(int, matches)))
  

output = 0
for row in inp:
  if solveEq(row):
    output += row[0]

print(output)