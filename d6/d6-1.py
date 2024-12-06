import re
import numpy as np

def move(line, index, dir):
  finished = False
  if dir == "up":
    while 0 <= line-1 < len(inp) and 0 <= index < len(inp[0]) and inp[line-1][index] != '#':
      inp[line][index] = 'X'
      line = line-1
    if 0 <= line-1 < len(inp) and 0 <= index < len(inp[0]):
      pass
    else:
      finished = True
    dir = "right"
  elif dir == "down":
    while 0 <= line+1 < len(inp) and 0 <= index < len(inp[0]) and inp[line+1][index] != '#':
      inp[line][index] = 'X'
      line = line+1
    if 0 <= line+1 < len(inp) and 0 <= index < len(inp[0]):
      pass
    else:
      finished = True
    dir = "left"
  elif dir == "right":
    while 0 <= line < len(inp) and 0 <= index+1 < len(inp[0]) and inp[line][index+1] != '#':
      inp[line][index] = 'X'
      index = index+1
    if 0 <= line < len(inp) and 0 <= index+1 < len(inp[0]):
      pass
    else:
      finished = True
    dir = "down"
  elif dir == "left":
    while 0 <= line < len(inp) and 0 <= index-1 < len(inp[0]) and inp[line][index-1] != '#':
      inp[line][index] = 'X'
      index = index-1
    if 0 <= line < len(inp) and 0 <= index-1 < len(inp[0]):
      pass
    else:
      finished = True
    dir = "up"
  return line, index, dir, finished


inp = []
starting_pos = 0
with open("input", 'r') as file:
  for line in file:
    inp.append(list(line.strip()))
    if starting_pos == 0:
      guard = line.find('^' or 'v' or '>' or '<')
      if guard !=-1:
        if line[guard]=='^':
          dir = "up"
        elif line[guard]=='v':
          dir = "down"
        elif line[guard]=='>':
          dir = "right"
        elif line[guard]=='<':
          dir = "left"

        starting_pos = (len(inp)-1, guard, dir)
        inp[-1][guard] = 'X'

finished = False
line, index, dir = starting_pos
while not finished:
  line, index, dir, finished = move(line, index, dir)

output = 0
for l in inp:
  output += l.count('X')

print(output+1)