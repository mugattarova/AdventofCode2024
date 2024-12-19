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
  time.sleep(0.2)

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

class keydefaultdict(defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError( key )
        else:
            ret = self[key] = self.default_factory(key)
            return ret

def path(prev, coord):
  total = [coord]
  while coord in prev:
    coord = prev[coord]
    total.insert(0, coord)
  return total

def h(x):
  return 0.5*math.sqrt((int(height-x.real)**2)+(int(width-x.imag)**2))

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
      return len(path(prev, coord))-1

    for delta_coord in [1, 1j, -1, -1j]:
      new_coord = coord + delta_coord
      if new_coord in grid and pscores[coord]+1 < pscores[new_coord]:
        prev[new_coord] = coord
        pscores[new_coord] = pscores[coord]+1
        heappush(q, (pscores[new_coord]+h(new_coord), r := r+1, new_coord))

  return -1

colorama_init()
inp = open('input', 'r').read().split('\n')
bytes = []
for line in inp:
   line = list(map(int, line.split(',')))
   bytes.append(line[1]+line[0]*1j)
height, width = 71, 71
total = 1024
start = 0+0j; end = (height-1) + (width-1)*1j
initbytes = bytes[:total]
grid = [i+j*1j for i in range(height)
               for j in range(width) if i+j*1j not in initbytes]

for i in range(total+1, len(bytes)):
  grid.remove(bytes[i])
  if a_star(grid) > 0: 
    print(i)
    continue
  else: 
    print(f"{bytes[i].imag},{bytes[i].real}")
    break