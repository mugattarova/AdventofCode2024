def issafe(line):
  difs = [line[i+1] - line[i] for i in range(len(line)-1)]
  if not all(0 < abs(d) < 4 for d in difs):
    return False

  inc = all(d>0 for d in difs)
  dec = all(d<0 for d in difs)
  
  if inc or dec:
    return True
  return False

def istoleratable(line):
  for i in range(len(line)):
    elem = line[i]
    del line[i]
    if issafe(line):
      return True
    line.insert(i, elem)
  
  return False

inputlines=[]
with open("input", 'r') as file:
  for line in file:
    intLine = list(map(int, line.strip().split()))
    inputlines.append(intLine)

outCount=0
for line in inputlines:
  if issafe(line):
    outCount+=1
  elif istoleratable(line):
    outCount+=1

print(outCount)