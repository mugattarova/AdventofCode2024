import re

def do_op(opcode, litoperand, comboperand):
  global rA, rB, rC, out, i, jumped
  match opcode:
    case 0: rA = rA//(2**comboperand)
    case 1: rB = rB^litoperand
    case 2: rB = comboperand%8
    case 3: 
      if rA!=0: i=litoperand; jumped = True
    case 4: rB = rB^rC
    case 5: out.append(comboperand%8)
    case 6: rB = rA//(2**comboperand)
    case 7: rC = rA//(2**comboperand)

def get_comboperand(operand):
  match operand:
    case 0|1|2|3: return operand
    case 4: return rA
    case 5: return rB
    case 6: return rC
    case 7: return None

def eval(A):
  return ((((A%8)^2)^(A//2**((A%8)^2)))^7)%8

def backtrack(prog, i, A):
  if i==len(prog)+1:
    return A
  for n in range(A*8, (A+1)*8):
    if eval(n) == prog[-i]:
      val = backtrack(prog, i+1, n)
      if val != None:
        return val
  return None

regs, prog = open('input', 'r').read().split('\n\n')
prog = list(map(int, re.findall("(\d+)", prog)))
i=0; jumped = False

rA=backtrack(prog, 1, 0); rB=0; rC=0; out = []
print(f'A={rA}')
# check
while True:
  if i<len(prog): 
    opcode = prog[i%len(prog)]
    litoperand = prog[(i+1)%len(prog)]
    comboperand = get_comboperand(litoperand)
  else: break
  do_op(opcode, litoperand, comboperand)

  if jumped: jumped = False
  else: i+=2

for x in out:
  print(f'{x},', end='')