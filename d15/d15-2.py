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
        warehouse.append(list(line.strip().replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')))
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
      return None
    case _:
      raise Exception("direction is represented wrong")

def get_left_of_box(boxy, boxx):
  match warehouse[boxy][boxx]:
    case '[':
      return [boxy, boxx]
    case ']':
      return [boxy, boxx-1]
    case _:
      return [boxy, boxx]

def can_move_box(dir, boxy, boxx):
  box = get_left_of_box(boxy, boxx)
  
  match dir:
    case '^':
      match (warehouse[box[0]-1][box[1]], warehouse[box[0]-1][box[1]+1]):
      # base case
        case ('.', '.'):
          return True
        case ('#', _) | (_, '#'):
          return False
      # more boxes
        case (']', '['):
          if can_move_box(dir, box[0]-1, box[1]) and can_move_box(dir, box[0]-1, box[1]+1):
            return True
          else:
            return False
        case ('.', '['):
          if can_move_box(dir, box[0]-1, box[1]+1):
            return True
          else:
            return False
        case (']', '.'):
          if can_move_box(dir, box[0]-1, box[1]):
            return True
          else:
            return False 
        case ('[', ']'):
          if can_move_box(dir, box[0]-1, box[1]):
            return True
          else:
            return False 
    case 'v':
      match (warehouse[box[0]+1][box[1]], warehouse[box[0]+1][box[1]+1]):
      # base case
        case ('.', '.'):
          return True
        case ('#', _) | (_, '#'):
          return False
      # more boxes
        case (']', '['):
          if can_move_box(dir, box[0]+1, box[1]) and can_move_box(dir, box[0]+1, box[1]+1):
            return True
          else:
            return False
        case ('.', '['):
          if can_move_box(dir, box[0]+1, box[1]+1):
            return True
          else:
            return False
        case (']', '.'):
          if can_move_box(dir, box[0]+1, box[1]):
            return True
          else:
            return False
        case ('[', ']'):
          if can_move_box(dir, box[0]+1, box[1]):
            return True
          else:
            return False 
    case '<':
      # base case
      match warehouse[box[0]][box[1]-1]:
        case '.':
          return True
        case '#':
          return False
      # more boxes
      if can_move_box(dir, box[0], box[1]-1):
        return True
      else:
        return False
    case '>':      
      # base case
      match warehouse[box[0]][box[1]+2]:
        case '.':
          return True
        case '#':
          return False
      # more boxes
      if can_move_box(dir, box[0], box[1]+2):
        return True
      else:
        return False
  
def move_box(dir, boxy, boxx):
  box = get_left_of_box(boxy, boxx)
  if warehouse[boxy][boxx] in ['.', '#']:
    return
  # check if there's space in the target location
  # insert if so
  match dir:
    case '^':
      left, right = warehouse[box[0]-1][box[1]], warehouse[box[0]-1][box[1]+1]
      if (left, right) == ('.', '.'):
        warehouse[box[0]-1][box[1]] = '['
        warehouse[box[0]-1][box[1]+1] = ']'
        warehouse[box[0]][box[1]] = '.'
        warehouse[box[0]][box[1]+1] = '.'
        return
    case 'v':
      left, right = warehouse[box[0]+1][box[1]], warehouse[box[0]+1][box[1]+1]
      if (left, right) == ('.', '.'):
        warehouse[box[0]+1][box[1]] = '['
        warehouse[box[0]+1][box[1]+1] = ']'
        warehouse[box[0]][box[1]] = '.'
        warehouse[box[0]][box[1]+1] = '.'
        return
    case '<':
      if warehouse[box[0]][box[1]-1] == '.':
        warehouse[box[0]][box[1]-1] = '['
        warehouse[box[0]][box[1]] = ']'
        warehouse[box[0]][box[1]+1] = '.'
        return
    case '>':
      if warehouse[box[0]][box[1]+2] == '.':
        warehouse[box[0]][box[1]+2] = ']'
        warehouse[box[0]][box[1]+1] = '['
        warehouse[box[0]][box[1]] = '.'
        return

  # cant immediately move, so call this on the next box
  match dir:
    case '^':
      move_box(dir, box[0]-1, box[1])
      move_box(dir, box[0]-1, box[1]+1)
    case 'v':
      move_box(dir, box[0]+1, box[1])
      move_box(dir, box[0]+1, box[1]+1)
    case '<':
      move_box(dir, box[0], box[1]-1)
    case '>':
      move_box(dir, box[0], box[1]+2)

  # after that space is free, call the move function on this box again
  move_box(dir, box[0], box[1])

warehouse, instr, (roboty, robotx) = get_input()

for i in range(len(instr)):
  # print(str(i)+" cycle "+instr[i])
  # print_grid(warehouse, roboty, robotx)
  dir = instr[i]
  coords = move_once(dir, roboty, robotx)
  if coords != None:
    newy, newx = coords
  else:
    continue

  match warehouse[newy][newx]:
    case '#':
      continue
    case '.':
      roboty, robotx = newy, newx
    case '[' | ']':
      if can_move_box(dir, newy, newx):
        move_box(dir, newy, newx)
        roboty, robotx = newy, newx

print_grid(warehouse, roboty, robotx)
output = 0
for i in range(len(warehouse)):
  for j in range(len(warehouse[0])):
    if warehouse[i][j] == '[':
      output += 100*i + j

print(output)