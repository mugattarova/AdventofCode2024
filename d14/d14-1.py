import re
import math

def get_input():
  inp = []
  with open("input", 'r') as file:
    for line in file:
      inp.append(list(map(int, re.findall('-?(?:\d+)+', line))))
  return inp
  
def calc_pos(p, v, len):
  if v >= 0:
    return (p + v*sec)%len
  else:
    return (len-(abs(p + v*sec)%len))%len


inp = get_input()
x, y = 101, 103
xmid, ymid = x//2, y//2
sec = 100
final_pos = []
quads = [0, 0, 0, 0]

for robot in inp:
  px = robot[0]
  py = robot[1]
  vx = robot[2]
  vy = robot[3]
  fin_x = calc_pos(px, vx, x)
  fin_y = calc_pos(py, vy, y)
  final_pos.append((fin_x, fin_y))

for (fin_x, fin_y) in final_pos:
  if fin_x < xmid and fin_y < ymid:
    quads[0] +=1
  elif fin_x < xmid and fin_y > ymid:
    quads[1] +=1
  elif fin_x > xmid and fin_y < ymid:
    quads[2] +=1
  elif fin_x > xmid and fin_y > ymid:
    quads[3] +=1

output = math.prod(quads)
print(output)