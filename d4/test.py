import numpy as np

inp=[]
with open("test", 'r') as file:
  for line in file:
    inp.append(list(line.strip()))

reversedinp = inp[::-1]

for line in reversedinp:
  print("".join(line).replace(" ", ""))