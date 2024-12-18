from collections import deque
import os

def to_dir(ch):
  return [-1, 1j, 1, -1j]['^>v<'.index(ch)]

def print_grid(grid, robot):
  imax, jmax = int(max(grid.keys(), key=lambda n:n.real).real), int(max(grid.keys(), key=lambda n:n.imag).imag)
  os.system('cls' if os.name == 'nt' else 'clear')
  for i in range(imax+2):
    for j in range(jmax+2):
      if i+j*1j == robot:
        print('@', end='')
      elif i+j*1j not in grid.keys():
        print('#', end='')
      else:
        print(grid[i+j*1j], end='')
    print()

_grid, _moves = open('input', 'r').read().split('\n\n')

grid = {i+j*1j: c for i,r in enumerate(_grid.split())
                  for j,c in enumerate(r.strip()) if c != '#'}

robot = [x for x in grid if grid[x] == '@'][0]
grid[robot] = '.'
moves = [l.replace('\n', '') for l in _moves]
print_grid(grid, robot)
while moves:
  # if len(moves)%100:
  move = to_dir(moves.pop(0))                                         # get cardinal move
  stack = deque(); i=1
  while True:                                # moves once every iteration, saves the current position
    cur_pos = (robot + move*i)
    if cur_pos not in grid:                                         # if hit an obstacle
      stack = deque()                                                 # empty stack
      i=0                                                            # reset i
      break
    elif grid[cur_pos] == '.':                                                # if position is free to move in
      while stack:                                                    # go down the box stack
        grid[box := stack.pop()] = '.'                                # old position is empty
        grid[box+move] = 'O'                                          # new position is a box
      robot += move                                                   # move the robot                                    
      break
    elif grid[cur_pos] == 'O':                                              # if this a box
      stack.append(cur_pos)                                           # push it onto the stack
    
    i+=1                                                              # increments the move number
  # print_grid(grid, robot)

print_grid(grid, robot)
print(sum([(x.real*100+x.imag) for x in grid if grid[x]=='O']))
