def get_input():
  warehouse = []
  instr = []
  instr_mode = False
  with open("input", 'r') as file:
    for line in file:
      if not instr_mode:
        if line.strip() == "":
          instr_mode = True
          continue
        warehouse.append(list(line.strip()))
        if '@' in warehouse[-1]:
          start = (len(warehouse)-1, warehouse[-1].index('@'))
          warehouse[-1][warehouse[-1].index('@')] = '.'
      else:
        for e in list((line.strip())):
          instr.append(e)
  return warehouse, instr, start

def print_grid(warehouse, roboty, robotx):
  for i in range(len(warehouse)):
    for j in range(len(warehouse[0])):
      if i==roboty and j==robotx:
        print('@', end='')
      else:
        print(warehouse[i][j], end='')
    print()

def move_once(dir, cury, curx):
  maxy = len(warehouse)
  maxx = len(warehouse[0])
  match dir:
    case '^':
      if (0 <= cury-1 <= maxy) and (0 <= curx <= maxx):
        return cury-1, curx
      return None
    case 'v':
      if (0 <= cury+1 <= maxy) and (0 <= curx <= maxx):
        return cury+1, curx
      return None     
    case '>':
      if (0 <= cury <= maxy) and (0 <= curx+1 <= maxx):
        return cury, curx+1
      return None
    case '<':
      if (0 <= cury <= maxy) and (0 <= curx-1 <= maxx):
        return cury, curx-1
    case _:
      raise Exception("direction is represented wrong")

warehouse, instr, (roboty, robotx) = get_input()

box = False

for i in range(len(instr)):
  # print(str(i)+" cycle "+instr[i])
  # print_grid(warehouse, roboty, robotx)
  cury, curx = roboty, robotx
  dir = instr[i]
  cursym = warehouse[cury][curx]
  while cursym != '#':
    coords = move_once(dir, cury, curx)
    if coords != None:
      newy, newx = coords
    else:
      box = False
      continue
    cursym = warehouse[newy][newx]
    match cursym:
      case '.':
        roboty, robotx = move_once(dir, roboty, robotx)
        warehouse[roboty][robotx] = '.'
        cursym = '#'
        if box:
          warehouse[newy][newx] = 'O'
          box = False
      case 'O':
        box = True
      case '#':
        box = False
        continue
    
    cury, curx = newy, newx


output = 0
for i in range(len(warehouse)):
  for j in range(len(warehouse[0])):
    if warehouse[i][j] == 'O':
      output += 100*i + j

print(output)