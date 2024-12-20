import math, os, time
from collections import defaultdict
from heapq import heappop, heappush
from colorama import init as colorama_init
from colorama import Fore, Back, Style

def print_grid(grid, scores, q):
  front = [coord for( _, _, coord) in q]
  os.system('cls' if os.name == 'nt' else 'clear')
  for i in range(height):
    for j in range(width):
        
      if i+j*1j in grid and scores[i+j*1j] < math.inf:
        if i+j*1j in front:
          print(f'{Back.GREEN} {Style.RESET_ALL}', end='')
        else:
          print(f'{Back.CYAN} {Style.RESET_ALL}', end='')
      elif i+j*1j in grid:
        print('.', end='')
      else:
        print(f'{Fore.MAGENTA}#{Style.RESET_ALL}', end='')
    print()
  time.sleep(0.3)

def print_path(grid, path):
  for i in range(height):
    for j in range(width):
        
      if i+j*1j in grid and i+j*1j in path:
          print(f'{Back.GREEN} {Style.RESET_ALL}', end='')
      elif i+j*1j in grid:
        print('.', end='')
      else:
        print('#', end='')
    print()

def h(x):
  return math.sqrt((int(end.real-x.real)**2)+(int(end.imag-x.imag)**2))

def path(prev, coord):
  total = [coord]
  while coord in prev:
    coord = prev[coord]
    total.insert(0, coord)
  return total

def a_star(grid):
  prev = dict()
  pscores = defaultdict(lambda: math.inf)
  pscores[start] = 0
  q = [(pscores[start]+h(start), r:=0, start)]

  while q:
    # vals = sorted(list(set(pscores.values())))
    # if len(vals) > 1 and vals[-2]%10 == 0:
    #   print_grid(grid, pscores, q)
    _, _, coord = heappop(q)

    if coord == end:
      return path(prev, coord)

    for delta_coord in [1, 1j, -1, -1j]:
      new_coord = coord + delta_coord
      if grid[new_coord]!='#' and pscores[coord]+1 < pscores[new_coord]:
        prev[new_coord] = coord
        pscores[new_coord] = pscores[coord]+1
        heappush(q, (pscores[new_coord]+h(new_coord), r := r+1, new_coord))

  return -1

grid = {i+j*1j: c for i, k in enumerate(open('input', 'r'))
                  for j, c in enumerate(k.strip())}
height = int(max([x.real for x in grid]))
width = int(max([x.imag for x in grid]))
start, = (e for e in grid if grid[e]=='S')
end, = (e for e in grid if grid[e]=='E')

path = a_star(grid)
nocheat = len(path)-1
path_enumer = {p:i for i,p in enumerate(path)}

output = 0

for p in path_enumer.keys():
  for delta in [-2, -1+1j, +2j, 1+1j, 2, 1-1j, -2j, -1-1j]:
    neig = p + delta
    if neig in grid and grid[neig] in ['.', 'E'] and path_enumer[p] < path_enumer[neig]:
      l = len(path[:path_enumer[p]+1] + path[path_enumer[neig]:])
      if nocheat - l >= 100:
        output+=1

print(output)