from functools import cache

@cache
def count_designs(d):
  global pat
  if d=='': return 1

  out=0
  for p in pat:
    if d[:len(p)] == p:
      out+=count_designs(d[len(p):])
  return out

pat, des = open('input', 'r').read().split('\n\n')
pat = pat.strip().split(', ')
des = des.strip().split('\n')

out = 0
for d in des:
  out+=count_designs(d)
print(out)
