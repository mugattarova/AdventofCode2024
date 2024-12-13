import re
import matplotlib.pyplot as plt
import numpy as np
from shapely import LineString
 

class ClawMachine():
  def __init__(self, buttonA, buttonB, goal):
    AX, AY = buttonA
    BX, BY = buttonB
    goalX, goalY = goal
    self.AX = int(AX)
    self.AY = int(AY)
    self.BX = int(BX)
    self.BY = int(BY)
    self.goalX = int(goalX)
    self.goalY = int(goalY)

  def bx_func(self, x):
    # given number of A presses, find the number of B presses
    return (self.goalX-(self.AX*x))/self.BX
  
  def by_func(self, y):
    # given number of A presses, find the number of B presses
    return (self.goalY-(self.AY*y))/self.BY

  def find_solution(self):
    def find_cost(point):
      Apress = point.x
      Bpress = point.y
      if (Apress == int(Apress)) and (Bpress == int(Bpress)) and (0 <= Bpress <= 100):
        return Apress*3 + Bpress
      return None
    
    num = np.arange(0, 101, 1)
    fx = self.bx_func(num)
    fy = self.by_func(num)
    
    first_line = LineString(np.column_stack((num, fx)))
    second_line = LineString(np.column_stack((num, fy)))
    intersection = first_line.intersection(second_line)

    cost = None
    if intersection.geom_type == 'MultiPoint':
      mincost = None
      for point in list(intersection.geoms):
        cost = find_cost(point)
        if mincost == None or cost < mincost:
          mincost = cost
      cost = mincost
    elif intersection.geom_type == 'Point':
      cost = find_cost(intersection)
    if cost == None:
      cost = 0
    return cost
    # for each intersect (x, y) on the graph, check int(n)==n

def get_input():
  inp = []
  with open("input", 'r') as file:
    file = file.read().replace('\n', ' ')
    buttonAs = re.findall('Button A: X\+(\d+), Y\+(\d+)', file)
    buttonBs = re.findall('Button B: X\+(\d+), Y\+(\d+)', file)
    prizes = list(re.findall('Prize: X=(\d+), Y=(\d+)', file))
    for i in range(len(buttonAs)):
      inp.append(ClawMachine(buttonAs[i], buttonBs[i], prizes[i]))
  return inp
  

inp = get_input()

output = 0
for cm in inp:
  output += cm.find_solution()

print(output)