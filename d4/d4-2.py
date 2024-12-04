import re
import numpy as np


def coordMAS(line):
  out = []
  line = str(line).replace(" ", "").replace("'", "").replace("\n", "")

  i=0
  while i < len(line):
    index = line[i:].find("MAS")
    if index>0:
      out.append(i+index)
      i += index+2
    else:
      break


  i=0
  while i < len(line):
    index = line[i:].find("SAM")
    if index>0:
      out.append(i+index)
      i += index+2
    else: 
      break

  return out


def getCoordFromDiag(diagpos, k, flipped, length):
  if not flipped:
    if k>0:
      return (diagpos, k+diagpos)
    elif k<0:
      k=-k
      return (k+diagpos, diagpos)
    elif k==0:
      return (diagpos, diagpos)
  else:
    # coord sum is the same always
    if k>0:
      sumcoord = length-1+k
      return (sumcoord-k-diagpos, k+diagpos)
    elif k<0:
      k=-k
      sumcoord = length-1-k
      return (sumcoord-diagpos, diagpos)
    elif k==0:
      sumcoord = length-1
      return (sumcoord-diagpos, diagpos)


def getCoordsInList(line, k, flipped, length):
  out = []
  coordslist = coordMAS(line)
  for c in coordslist:
    out.append(getCoordFromDiag(c, k, flipped, length))
  return out


output=0
inp = []
with open("input", 'r') as file:
  for line in file:
    inp.append(list(line.strip()))
inp = np.array(inp)
print("File processed")
print()


# find all MAS in both directions
# record abs coordinates
# cross (hehe) check both lists for the same absolute locations of middle A

diag_topleftstart_coords = []
flagUp = True
diag_topleftstart_coords.extend(getCoordsInList(np.diag(inp), 0, False, len(inp[0])))
i = 1
while flagUp:
  diag_topleftstart_coords.extend(getCoordsInList(np.diag(inp, k=i), i, False, len(inp[0])))
  diag_topleftstart_coords.extend(getCoordsInList(np.diag(inp, k=-i), -i, False, len(inp[0])))
  if len(np.diag(inp,k=i))<=3:
    flagUp = False
  i += 1

diag_toprightstart_coords = []
inversed_inp = inp[::-1].copy()
flagUp = True
diag_toprightstart_coords.extend(getCoordsInList(np.diag(inversed_inp), 0, True, len(inversed_inp[0])))
i = 1
while flagUp:
  diag_toprightstart_coords.extend(getCoordsInList(np.diag(inversed_inp, k=i), i, True, len(inp[0])))
  diag_toprightstart_coords.extend(getCoordsInList(np.diag(inversed_inp, k=-i), -i, True, len(inp[0])))
  if len(np.diag(inp,k=i))<=3:
    flagUp = False
  i += 1

outlist = []
for coord in diag_topleftstart_coords:
  if coord in diag_toprightstart_coords:
    output += 1
    outlist.append(coord)


print(output)
print(outlist)