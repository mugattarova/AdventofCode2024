import numbers
from collections import defaultdict
from functools import cache

def num_to_dir(code):
  out = defaultdict(int)
  curb = 'A'
  code = list(code)
  while code:
    row = []
    endb = code.pop(0)
    dif = numpad[endb]-numpad[curb]
    #walks through empty zone
    if through_empty_numpad(numpad[curb], numpad[endb], 3+0j):
      if dif.real <= 0:
        append_non0(row, dif.real)  
      if dif.imag < 0:
        append_non0(row, dif.imag*1j)
      if dif.imag >= 0:
        append_non0(row, dif.imag*1j)
      if dif.real > 0:
        append_non0(row, dif.real)
    # does not walk through empty zone
    else:
      if dif.imag < 0:
        append_non0(row, dif.imag*1j)
      if dif.real > 0:
        append_non0(row, dif.real)
      if dif.real <= 0:
        append_non0(row, dif.real)    
      if dif.imag >= 0:
        append_non0(row, dif.imag*1j)
    out[tuple(row+['A'])]+=1
    curb = endb
  return out

def through_empty_numpad(p1, p2, empty):
  return (max(p1.real, p2.real)==empty.real and min(p1.imag, p2.imag)==empty.imag)

def through_empty_robopad(p1, p2, empty):
  return (min(p1.real, p2.real)==empty.real and min(p1.imag, p2.imag)==empty.imag)

def sum_values_complex(elem):
  return int(abs(elem.real))+int(abs(elem.imag))

def append_non0(out, elem):
  if isinstance(elem, numbers.Number):
    if elem!=0:
      out.append(elem)
  else:
    out+=elem

@cache
def dir_to_dir_dict(code):
  out = []
  code = list(code)
  curb = 'A'
  while code:
    row = []
    instr = code.pop(0)
    if instr!='A':
      bpress = sum_values_complex(instr)
      endb = instr/bpress
    else:
      bpress = 1
      endb = 'A'
    dif = robopad[endb] - robopad[curb]
    if through_empty_robopad(robopad[curb], robopad[endb], 0+0j):
      if dif.real > 0:
        append_non0(row, dif.real)
      if dif.imag < 0:
        append_non0(row, dif.imag*1j)
      if dif.imag > 0:
        append_non0(row, dif.imag*1j)
      if dif.real < 0:
        append_non0(row, dif.real)  
    else:
      if dif.imag < 0:
        append_non0(row, dif.imag*1j)
      if dif.real > 0:
        append_non0(row, dif.real)
      if dif.real < 0:
        append_non0(row, dif.real)    
      if dif.imag > 0:
        append_non0(row, dif.imag*1j)
    row.append('A')
    curb = endb
    out.append(tuple(row))
    [out.append('A') for x in range(bpress-1)]
  return out

def dir_to_dir(instr: dict):
  counter = defaultdict(int)
  for line in instr.keys():
    if instr[line]!=0:
      for unfold_line in dir_to_dir_dict(line):
        counter[unfold_line] += instr[line]
  return counter

def count_len(code):
  out = 0
  for snip in code.keys():
    lsnip = list(snip)
    snip_count = 0
    while lsnip:
      elem = lsnip.pop(0)
      if isinstance(elem, numbers.Number):
        for i in range(sum_values_complex(elem)): snip_count+=1
      else:
        snip_count+=1
    out+=snip_count*code[snip]
  return out

codes = [x for x in open('input', 'r').read().strip().split('\n')]
numpad = { 7:0+0j, 8:0+1j, 9:0+2j, 4:1+0j, 5:1+1j, 6:1+2j, 1:2+0j, 2:2+1j, 3:2+2j, 0:3+1j, 'A':3+2j }
robopad = { -1:0+1j, 'A':0+2j, -1j:1+0j, 1:1+1j, 1j:1+2j }

output = 0
for code in codes:
  num = int(code[:-1])
  code = num_to_dir([int(x) for x in code if x!='A']+['A'])
  for i in range(25):
    code = dir_to_dir(code)
  output += num*count_len(code)
print(output)