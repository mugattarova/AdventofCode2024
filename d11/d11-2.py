from collections import defaultdict


def get_input():
  inp = []
  with open("input", 'r') as file:
    for line in file:
      inp = list(map(int, list(line.strip().split())))
       
  return inp

def apply_rules(num):
  digits = len(str(num))
  if num == 0:
    return [1]
  elif digits%2 == 0:
    left = int(str(num)[:digits//2])
    right = int(str(num)[digits//2:])
    return [left, right]
  else:
    return [num*2024]

def run_iters(num, iters):
  arr = [num]
  temp = []

  for i in range(iters):
    for j in range(len(arr)):
      elem = apply_rules(arr.pop(0))
      while elem:
        temp.append(elem.pop(0))
    arr = temp
    temp = []
  
  return arr

def build_lookup_table():
  # number of iters the table jumps to
  iters = 6
  lookup_table = dict()
  
  # first 0-99 numbers can be looked up
  for i in range(100):
    lookup_table[i] = run_iters(i, iters)

  return lookup_table

class keydefaultdict(defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError( key )
        else:
            ret = self[key] = self.default_factory(key)
            return ret

inp = get_input()
lookup_table = keydefaultdict(apply_rules)
counter = defaultdict(int)
temp_counter = defaultdict(int)

for elem in inp:
  counter[elem] = 1

for i in range(75):
  print(i)
  nums = list(counter.keys())
  for num in nums:
    res = lookup_table[num]
    for r in res:
      temp_counter[r] += counter[num]
  counter = temp_counter
  temp_counter = defaultdict(int)


print(sum(counter.values()))