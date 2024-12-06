import re
import numpy as np

def move(line, index, dir, cur_inp, turns):
  finished = False
  looped = False
  turn = []


  if dir == "up":
    while 0 <= line-1 < len(cur_inp) and 0 <= index < len(cur_inp[0]) and cur_inp[line-1][index] != '#':
      line = line-1
    if 0 <= line-1 < len(cur_inp) and 0 <= index < len(cur_inp[0]):
      pass
    else:
      finished = True
    dir = "right"
    turn = (line, index, "up", "right")


  elif dir == "down":
    while 0 <= line+1 < len(cur_inp) and 0 <= index < len(cur_inp[0]) and cur_inp[line+1][index] != '#':
      line = line+1
    if 0 <= line+1 < len(cur_inp) and 0 <= index < len(cur_inp[0]):
      pass
    else:
      finished = True
    dir = "left"
    turn = (line, index, "down", "left")


  elif dir == "right":
    while 0 <= line < len(cur_inp) and 0 <= index+1 < len(cur_inp[0]) and cur_inp[line][index+1] != '#':
      index = index+1
    if 0 <= line < len(cur_inp) and 0 <= index+1 < len(cur_inp[0]):
      pass
    else:
      finished = True
    dir = "down"
    turn = (line, index, "right", "down")


  elif dir == "left":
    while 0 <= line < len(cur_inp) and 0 <= index-1 < len(cur_inp[0]) and cur_inp[line][index-1] != '#':
      index = index-1
    if 0 <= line < len(cur_inp) and 0 <= index-1 < len(cur_inp[0]):
      pass
    else:
      finished = True
    dir = "up"
    turn = (line, index, "left", "up")


  if turn in turns:
    looped = True
  else:
    turns.append(turn)
  return line, index, dir, turns, finished, looped


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
        inp[-1][guard] = '.'

output = 0
for i in range(len(inp)):
  for j in range(len(inp[0])):
    line, index, dir = starting_pos
    if inp[i][j] != '#' or (i!=line and j!=index):
      print("at ")
      inp_test = [l[:] for l in inp]
      inp_test[i][j] = '#'
      looped, finished = 0, 0
      turns = []

      while (not looped) and (not finished):
        line, index, dir, turns, finished, looped = move(line, index, dir, inp_test, turns)
      if looped:
        output += 1


print(output)