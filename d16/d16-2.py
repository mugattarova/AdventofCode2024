from collections import defaultdict
from itertools import starmap
import math
import numpy as np
from heapq import heappush, heappop
from functools import total_ordering

@total_ordering
class Direction:
  def __init__(self, vector, numeric):
    self.vector = vector
    self.numeric = numeric

  def __eq__(self, other):
    return self.numeric == other.numeric
    
  def __lt__(self, other):
    return self.numeric < other.numeric

class CARDINAL_DIRECTIONS:
  NORTH = Direction((-1, 0), 0)
  EAST = Direction((0, 1), 1)
  SOUTH = Direction((1, 0), 2)
  WEST = Direction((0, -1), 3)

  _numeric_to_direction = {direction.numeric: direction for direction in [NORTH, EAST, SOUTH, WEST]}
  _vector_to_numeric = {direction.vector: direction.numeric for direction in [NORTH, EAST, SOUTH, WEST]}

  @classmethod
  def get_dir_by_num(cls, num):
    return cls._numeric_to_direction.get(num, None)

  @classmethod  
  def get_opposite(cls, num):
    return cls._numeric_to_direction.get((num+2)%4, None)
  
  @classmethod
  def num_by_vector(cls, vector):
    return cls._vector_to_numeric.get(vector, None)

def get_input(f):
  inp = []
  with open(f, 'r') as file:
    for line in file:
      linelist = list(line.strip())
      if 'S' in linelist:
        start = (len(inp), linelist.index('S'))
        linelist[:] = ['.' if x=='S' else x for x in linelist]
      if 'E' in linelist:
        end = (len(inp), linelist.index('E'))
        linelist[:] = ['.' if x=='E' else x for x in linelist]
      inp.append(linelist)

  return inp, start, end

def get_by_tuple(_arr, _tuple):
  line, index = _tuple
  return _arr[line][index]

def turn(cur_dir, clockwise: bool):
  if clockwise:
    return CARDINAL_DIRECTIONS.get_dir_by_num((cur_dir.numeric + 1) % 4)
  else:
    return  CARDINAL_DIRECTIONS.get_dir_by_num((cur_dir.numeric - 1) % 4)

def get_score(ctile, cdirection, newtile):
  if newtile == tuple(np.add(ctile, CARDINAL_DIRECTIONS.get_dir_by_num(cdirection).vector)):
    return 1
  elif newtile == tuple(np.add(ctile, CARDINAL_DIRECTIONS.get_opposite(cdirection).vector)):
    return 2001
  else:
    return 1001

def dijkstras(grid, start, stdir):
  q = []
  #       (score, position, direction)
  heappush(q, (0, start, stdir)) # East
  score = defaultdict(lambda: math.inf)
  prev = defaultdict(lambda: [])
  score[(*start, stdir)] = 0

  while q:
    cscore, tile, cdirection = heappop(q)
    for neigh in cardinal_neigh(tile, grid):
      if get_by_tuple(grid, neigh) != '#':
        alt = score[(*tile, cdirection)] + get_score(tile, cdirection, neigh)
        newdir = CARDINAL_DIRECTIONS.num_by_vector(tuple(np.subtract(neigh, tile)))
        if alt < score[(*neigh, newdir)]:
          if newdir != cdirection:
            prev[(*tile, newdir)].append((*tile, cdirection))
            score[(*tile, newdir)] = alt-1
            prev[(*neigh, newdir)].append((*tile, newdir))
            score[(*neigh, newdir)] = alt
          else:
            prev[(*neigh, newdir)] = [(*tile, cdirection)]
            score[(*neigh, newdir)] = alt
          heappush(q, (alt, neigh, newdir))
        elif alt == score[(*neigh, newdir)]:
          if newdir != cdirection:
            prev[(*tile, newdir)].append((*tile, cdirection))
            score[(*tile, newdir)] = alt-1
            prev[(*neigh, newdir)].append((*tile, newdir))
          else:
            prev[(*neigh, newdir)].append((*tile, cdirection))
          heappush(q, (alt, neigh, newdir))
  print(prev[(*end, 0)])
  print(prev[(*end, 1)])
  print(prev[(*end, 2)])
  print(prev[(*end, 3)])
  return score, prev

def cardinal_neigh(tile, grid):
  line, ind = tile
  neighs = map(lambda x: (line+x[0], ind+x[1]), [(-1, 0), (0, 1), (1, 0), (0, -1)])
  return [x for x in neighs if (0 <= x[0] < len(grid) and 0 <= x[1] < len(grid[0]))]

endscore = 11048
grid, start, end = get_input("input")
forwardscore, forwardprev = dijkstras(grid, start, 1)
print(forwardscore[(*end, 0)])
backscore, backprev = dijkstras(grid, end, 2)
print(backscore[(*start, 3)])
points = set()
output = 0
for i in range(len(grid)):
  for j in range(len(grid[0])):
    for i, j, direc in [(i, j, direc) for direc in [0, 1, 2, 3]]:
      fs = forwardscore[i, j, direc]
      bs = backscore[i, j, CARDINAL_DIRECTIONS.get_opposite(direc).numeric]
      if ((i, j) not in points) and fs!=math.inf and bs!=math.inf and ((fs + bs) == forwardscore[(*end, 0)]):
        points.add((i, j))
        output += 1

print(output)