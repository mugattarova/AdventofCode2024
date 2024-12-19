def count_designs(pat, des):
  out = 0
  for d in des:
    if check_design(pat, d):
      out += 1
  return out

def check_design(pat, d):
  tracker = [False] * (len(d)+1)
  tracker[0] = True
  
  for i in range(1, len(d)+1):
    for j in range(i):
      if tracker[j] and d[j:i] in pat:
        tracker[i] = True
        break
  
  return tracker[-1]

pat, des = open('input', 'r').read().split('\n\n')
pat = pat.strip().split(', ')
des = des.strip().split('\n')

print(count_designs(pat, des))