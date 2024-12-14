import re
import matplotlib.pyplot as plt
from collections import defaultdict

def get_input():
  inp = []
  with open("input", 'r') as file:
    for line in file:
      inp.append(list(map(int, re.findall('-?(?:\d+)+', line))))
  return inp
  
def calc_pos(p, v, len, sec):
  if v >= 0:
    return (p + v*sec)%len
  else:
    return (len-(abs(p + v*sec)%len))%len
  
def has_border(coords):
  for i in range(x):
    if ((i, 0) not in coords) or ((i, y-1) not in coords):
      return False
  for i in range(y):
    if ((0, i) not in coords) or ((x-1, i) not in coords):
      return False
  return True

def is_25percent_empty(coords):
  coords = set(coords)
  if len(coords) > 7803:
    return False
  return True

def is_xmas_tree(coords):
  coords = set(coords)
  tree_set = set()

  for i in range(x):
    tree_set.add((i, 0))
    tree_set.add((i, y-1))
  for i in range(y):
    tree_set.add((0, i))
    tree_set.add((x-1, i))

def print_grid(coords):
  for cy in range(y):
    for cx in range(x):
      if (cx, cy) in coords:
        print('0', end='')
      else:
        print(' ', end='')
    print()


def max_cluster(coords):
  def dfs(locx, locy):
    nonlocal cluster

    if locx < 0 or locx >= cols or locy < 0 or locy >= rows:
      return

    if (locx, locy) not in coords:
      return

    if (locx, locy) not in visited:
      cluster += 1
      visited.add((locx, locy))

      dfs(locx + 1, locy)
      dfs(locx - 1, locy)
      dfs(locx, locy + 1)
      dfs(locx, locy - 1)

  sx, sy = coords[0]
  rows, cols = y, x
  coords = set(coords)
  visited = set()
  # start with a random point
  # start filling it
  # only when coords == visited stop
  # print the largest cluster 
  cluster_groups = []

  while coords != visited:
    for point in coords:
      if point not in visited:
        sx, sy = point

    cluster = 0
    dfs(sx, sy)
    cluster_groups.append(cluster)

  return max(cluster_groups)


inp = get_input()
x, y = 101, 103
final_pos = []
connect_num = 10

for i in range(0, 10000):
  for robot in inp:
    px = robot[0]
    py = robot[1]
    vx = robot[2]
    vy = robot[3]
    fin_x = calc_pos(px, vx, x, i)
    fin_y = calc_pos(py, vy, y, i)
    final_pos.append((fin_x, fin_y))
  
  if i%1000 == 0:
    print("Seconds elapsed: "+str(i))

  if max_cluster(final_pos) > 50:
    print("Seconds elapsed: "+str(i))
    print_grid(final_pos)
    input("Cluster found")

  final_pos = []
