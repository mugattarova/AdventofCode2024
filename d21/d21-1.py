import numbers

def num_to_dir(code):
  out = []
  curb = 'A'
  code = list(code)
  while code:
    endb = code.pop(0)
    dif = numpad[endb]-numpad[curb]
    #walks through empty zone
    if max(numpad[curb].real, numpad[endb].real)==3 and min(numpad[curb].imag, numpad[endb].imag)==0:
      if dif.real <= 0:
        append_non0(out, dif.real)  
      if dif.imag < 0:
        append_non0(out, dif.imag*1j)
      if dif.imag >= 0:
        append_non0(out, dif.imag*1j)
      if dif.real > 0:
        append_non0(out, dif.real)
    else:
      if dif.imag < 0:
        append_non0(out, dif.imag*1j)
      if dif.real > 0:
        append_non0(out, dif.real)
      if dif.imag >= 0:
        append_non0(out, dif.imag*1j)
      if dif.real <= 0:
        append_non0(out, dif.real)    
    out.append('A')
    curb = endb
  return out

def instr_imag(curb, endinstr, out):
  if endinstr.imag == 0: return curb
  _out = []
  if endinstr.imag < 0:
    endb = -1j
  else:
    endb = 1j
  _out.append(robopad[endb]-robopad[curb])
  [_out.append('A') for x in range(int(abs(endinstr.imag)))]
  append_non0(out, _out)
  return endb

def instr_real(curb, endinstr, out):
  if endinstr.real == 0: return curb
  _out = []
  if endinstr.real < 0:
    endb = -1
  else:
    endb = 1
  _out.append(robopad[endb]-robopad[curb])
  [_out.append('A') for x in range(int(abs(endinstr.real)))]
  append_non0(out, _out)
  return endb

def append_non0(out, elem):
  if isinstance(elem, numbers.Number):
    if elem!=0:
      out.append(elem)
  else:
    out+=elem

def dir_to_dir(code):
  out = []
  curb = 'A'
  while code:
    endinstr = code.pop(0)
    if endinstr!='A':
      if endinstr.imag < 0:                       # if left button needs to be pressed
        curb = instr_imag(curb, endinstr, out)    # press it first
        curb = instr_real(curb, endinstr, out)    
      elif endinstr.real > 0:
        curb = instr_real(curb, endinstr, out)
        curb = instr_imag(curb, endinstr, out)
      else:
        curb = instr_real(curb, endinstr, out)
        curb = instr_imag(curb, endinstr, out)
    else:
      out.append(robopad[endinstr]-robopad[curb])
      out.append('A')
      curb = 'A'
  
  return out
    
def count_len(code):
  out = 0
  while code:
    elem = code.pop(0)
    if isinstance(elem, numbers.Number):
      for i in range(int(abs(elem.real))+int(abs(elem.imag))): out+=1
    else:
      out+=1
  return out

def get_num(code):
  num = ''.join(str(x) for x in code[:-1])
  return int(num)

codes = [x for x in open('input', 'r').read().strip().split('\n')]
numpad = { 7:0+0j, 8:0+1j, 9:0+2j, 4:1+0j, 5:1+1j, 6:1+2j, 1:2+0j, 2:2+1j, 3:2+2j, 0:3+1j, 'A':3+2j }
robopad = { -1:0+1j, 'A':0+2j, -1j:1+0j, 1:1+1j, 1j:1+2j }

output = 0
for code in codes:
  code = [int(x) for x in code if x!='A']+['A']
  path = dir_to_dir(dir_to_dir(num_to_dir(code)))
  output += get_num(code)*count_len(path)

print(output)