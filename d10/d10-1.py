from itertools import starmap, product

def get_input():
  inp = []
  zeros = []
  with open("input", 'r') as file:
    for line in file:
      matches = list(map(int, list(line.strip())))
      inp.append(matches)

      curzeros = [i for i in range(0,len(matches)) if matches[i]==0]
      for elem in curzeros:
        zeros.append((len(inp)-1, elem))
    
  return inp, zeros

def find_trail(point):
  x, y = point
  working_list = {(0, x, y)}
  nines = set()

  while working_list:
    num, cx, cy = working_list.pop()
    # neighbours = list(starmap(lambda a, b: (cx+a, cy+b), product((0, 1, -1), (0, 1, -1))))[1:]
    neighbours = [(cx-1, cy), (cx, cy+1), (cx+1, cy), (cx, cy-1)]

    for n, m in neighbours:
      if 0<=n<len(inp) and 0<=m<len(inp[0]):
        neib = inp[n][m]
        if neib == num+1:
          if neib == 9:
            nines.add((n,m))
          else:
            working_list.add((num+1, n, m))

  return len(nines)

  
inp, zeros = get_input()
  

output = 0
for point in zeros:
  output += find_trail(point)

print(output)