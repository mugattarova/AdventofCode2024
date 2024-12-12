from collections import defaultdict
from math import sqrt

def group_plants(table):
  out = defaultdict(lambda: [])
  for i in range(len(table)):
    for j in range(len(table[0])):
      out[table[i][j]].append((i, j))
  
  return out

def find_perimeter(shape: list):
  edge_list = []
  edge_count = 0
  for x, y in shape:
    edges = [(x, y, x, y+1), (x, y+1, x+1, y+1), (x+1, y, x+1, y+1), (x, y, x+1, y)]
    for e in edges:
      if e not in edge_list: 
        edge_list.append(e)
        edge_count += 1
      else:
        edge_list.remove(e)
        edge_count -= 1

  return edge_count*len(shape)


def group_into_shapes(points):
  def is_contiguous(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) <= 1

  def dfs(point, group):
    group.append(point)
    visited.add(point)
    for neighbor in points:
      if neighbor not in visited and is_contiguous(point, neighbor):
        dfs(neighbor, group)

  visited = set()
  groups = []

  for point in points:
    if point not in visited:
      group = []
      dfs(point, group)
      groups.append(group)

  return groups
  
def get_input():
  inp = []
  with open("input", 'r') as file:
    for line in file:
      matches = list(list(line.strip()))
      inp.append(matches)
  return inp
  
inp = get_input()
plants = group_plants(inp)

output = 0
for key in plants.keys():
  for elem in group_into_shapes(plants[key]):
    output += find_perimeter(elem)
  
print(output)