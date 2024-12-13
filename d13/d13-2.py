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
    self.goalX = int(goalX)+10000000000000
    self.goalY = int(goalY)+10000000000000

  def bx_func(self, x):
    # given number of A presses, find the number of B presses
    return (self.goalX-(self.AX*x))/self.BX
  
  def by_func(self, y):
    # given number of A presses, find the number of B presses
    # res = (self.goalY-(self.AY*y))/self.BY
    return (self.goalY-(self.AY*y))/self.BY

  def find_solution(self):
    AX = self.AX
    AY = self.AY
    BX = self.BX
    BY = self.BY
    goalX = self.goalX
    goalY = self.goalY
    Apress = (goalX*BY - goalY*BX)/(AX*BY - AY*BX)
    Bpress = self.bx_func(Apress)
    if Apress == int(Apress) and Apress >=0 and Bpress == int(Bpress) and Bpress >= 0:
      return Apress*3 + Bpress
    return 0
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