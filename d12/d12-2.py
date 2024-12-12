from collections import defaultdict
from math import sqrt
import numpy as np

def group_plants(table):
  out = defaultdict(lambda: [])
  for i in range(len(table)):
    for j in range(len(table[0])):
      out[table[i][j]].append((i, j))
  
  return out



def find_price(shape: list):
  def get_edges(shape):
    edge_list = []

    for x, y in shape:
      edges = [(x, y, x, y+1, False), (x, y+1, x+1, y+1, False), (x+1, y, x+1, y+1, True), (x, y, x+1, y, True)]
      for (e1, e2, e3, e4, dir) in edges:
        e = (e1, e2, e3, e4)
        if (*e, not dir) not in edge_list: 
          edge_list.append((*e, dir))
        else:
          edge_list.remove((*e, not dir))
    return edge_list

  def combine_sides(arr):
    changed = True  # To track if any merge happens
    while changed:
        changed = False  # Reset flag for this pass
        new_arr = []
        i = 0
        
        while i < len(arr):
            if i < len(arr) - 1 and arr[i][1] == arr[i + 1][0]:  # Check if a merge is possible
                new_arr.append([arr[i][0], arr[i + 1][1]])  # Merge the pair
                i += 2  # Skip the next element since it's already merged
                changed = True  # Set flag to True as a merge happened
            else:
                new_arr.append(arr[i])  # If no merge, keep the element
                i += 1
        
        arr = new_arr  # Update the array with the merged result
    
    return arr


  edge_list = get_edges(shape)
  hor_sides = defaultdict(list)
  ver_sides = defaultdict(list)

  for edge in edge_list:
    x1, y1, x2, y2, dir = edge
    
    if x1==x2:
      # horizontal
      miny = min(y1, y2)
      maxy = max(y1, y2)
      delete = None
      newelem = None
      if hor_sides[(x1, dir)] != []:
        for i in range(len(hor_sides[(x1, dir)])):

          st, fin = hor_sides[(x1, dir)][i]
          if st == maxy:
            delete = i
            newelem = [miny, fin]

          elif fin == miny:
            delete = i
            newelem = [st, maxy]
          

      if delete != None:
        del hor_sides[(x1, dir)][i]
      if newelem == None:  
        hor_sides[(x1, dir)].append([miny, maxy])
      else:
        hor_sides[(x1, dir)].append(newelem)

    elif y1==y2:
    # vertical
      minx = min(x1, x2)
      maxx = max(x1, x2)
      delete = None
      newelem = None
      if ver_sides[(y1, dir)] != []:
        for i in range(len(ver_sides[(y1, dir)])):

          st, fin = ver_sides[(y1, dir)][i]
          if st == maxx:
            delete = i
            newelem = [minx, fin]

          elif fin == minx:
            delete = i
            newelem = [st, maxx]

      if delete != None:
        del ver_sides[(y1, dir)][i]
      if newelem == None:  
        ver_sides[(y1, dir)].append([minx, maxx])
      else:
        ver_sides[(y1, dir)].append(newelem)


  out = 0
  for key in hor_sides.keys():
    hor_sides[key] = combine_sides(hor_sides[key])
    out += len(hor_sides[key])
  for key in ver_sides.keys():
    ver_sides[key] = combine_sides(ver_sides[key])
    out += len(ver_sides[key])
  
  return out*len(shape)


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
    price = find_price(elem)
    print(key+": "+str(price))
    output += price
  
print(output)