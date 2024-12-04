import re
import numpy as np


def countXMAS(line):
  out = 0
  line = str(line).replace(" ", "").replace("'", "").replace("\n", "")
  out += line.count("XMAS")
  out += line.count("SAMX")
  return out


output=0
inp = []
with open("input", 'r') as file:
  for line in file:
    inp.append(list(line.strip()))
inp = np.array(inp)
print("File processed")
print()


# find in rows  
for line in inp:
  output += countXMAS(line)
print("Rows analyzed")
print("Output so far: "+str(output))
print()

# find in columns
for i in range(len(inp[0])):
  output += countXMAS(inp[:, i])
print("Columns analyzed")
print("Output so far: "+str(output))
print()

# find in top left to bottom right diagonals
flagUp = True
output += countXMAS(np.diag(inp))
i = 1
while flagUp:
  output += countXMAS(np.diag(inp,k=i))
  output += countXMAS(np.diag(inp,k=-i))
  if len(np.diag(inp,k=i))<=1:
    flagUp = False
  i += 1
print("Primary diags analyzed")
print("Output so far: "+str(output))
print()
  
# find in top right to bottom left diagonals
flagUp = True
inversed_inp = inp[::-1].copy()
output += countXMAS(np.diag(inversed_inp))
i = 1
while flagUp:
  output += countXMAS(np.diag(inversed_inp,k=i))
  output += countXMAS(np.diag(inversed_inp,k=-i))
  if len(np.diag(inversed_inp,k=i))<=1:
    flagUp = False
  i += 1
print("Inversed diags analyzed")
print("Output so far: "+str(output))
print()

print(output)