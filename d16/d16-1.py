import numpy as np
import heapq
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

  @classmethod
  def get_dir_by_num(cls, given_num):
    return cls._numeric_to_direction.get(given_num, None)

def get_input():
  inp = []
  with open("input", 'r') as file:
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

def dijkstras(grid, start, end):
  rows, cols = len(grid), len(grid[0])

  # priority queue
  q = []
  #                (score, position, direction)
  heapq.heappush(q,  (0,   start,    CARDINAL_DIRECTIONS.EAST.numeric)) 

  visited = set()
  visited.add((*start, CARDINAL_DIRECTIONS.EAST.numeric))

  while q:
    score, cur_position, cur_direction = heapq.heappop(q)
    cur_direction = CARDINAL_DIRECTIONS.get_dir_by_num(cur_direction)

    if cur_position == end:
      return score

    new_row, new_col = (np.add(cur_position, cur_direction.vector))
    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != '#':
      state = (new_row, new_col, cur_direction.numeric)
      if state not in visited:
        visited.add(state)
        heapq.heappush(q, (score + 1, (new_row, new_col), cur_direction.numeric))

    clockwise_dir = turn(cur_direction, True)
    state = (*cur_position, clockwise_dir.numeric)
    if state not in visited:
      visited.add(state)
      heapq.heappush(q, (score + 1000, cur_position, clockwise_dir.numeric))

    counterclockwise_dir = turn(cur_direction, False)
    state = (*cur_position, counterclockwise_dir.numeric)
    if state not in visited:
      visited.add(state)
      heapq.heappush(q, (score + 1000, cur_position, counterclockwise_dir.numeric))

  return -1

output = dijkstras(*get_input())

print(output)