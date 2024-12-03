import re

def multsRes(substring):
  out=0
  matches = re.findall('mul\((\d+),\s*(\d+)\)', substring)
  for x, y in matches:
    out+=int(x)*int(y)
  return out

output=0
with open("input", 'r') as file:
  input = file.read()

startind = 0
domode = True
while "don't()" in input[startind:] or "do()" in input[startind:]:
  if domode:
    endind = input[startind:].find("don't()")
    if endind != -1:
      endind+=startind
      output+=multsRes(input[startind:endind])
      startind = endind + 7
      domode = False
    else:
      output+=multsRes(input[startind:])
      startind = len(input) - 2
      break
  else:
    endind = input[startind:].find("do()")
    if endind != -1:
      endind+=startind      
      startind = endind + 4
      domode = True
    else:
      startind = len(input) - 2
      break
  print("output so far: "+str(output))



print(output)