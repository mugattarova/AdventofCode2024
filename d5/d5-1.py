import re
import numpy as np

def followsrule(rule, line):
  x, y = rule
  if x in line and y in line:
    if line.index(x) < line.index(y):
      return True
    else:
      return False
  else:
    return True

instruct = []
pages = []
switchreadmode = False
with open("input", 'r') as file:
  for line in file:
    if line.strip() == "":
      switchreadmode = True
    if not switchreadmode:
      instructmatches = re.findall('\d+', line)
      instructmatches = list(instructmatches)
      instruct.append((int(instructmatches[0]), int(instructmatches[1])))
    else:
      pagematches = re.findall('\d+', line)
      if line.strip() != "":
        pages.append(list(map(int, pagematches)))

output = 0
rulebroken = False
for update in pages:
  for rule in instruct:
    if not followsrule(rule, update):
      rulebroken = True
      break

  if rulebroken:
    rulebroken = False
  else:
    output += update[(len(update)-1)//2]

print(output)