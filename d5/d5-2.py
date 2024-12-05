import re
import numpy as np
from collections import defaultdict, deque

def followsrule(rule, line):
  x, y = rule
  if x in line and y in line:
    if line.index(x) < line.index(y):
      return True
    else:
      return False
  else:
    return True

def rulesforupdate(line):
  rules = []
  for x, y in instruct:
    if x in line and y in line:
      rules.append((x, y))
  return rules

def defaultz():
  return 0

class Graph:
  def __init__(self, n):
    self.n = n
    self.adjlist = defaultdict(list)
    self.indegree = defaultdict(defaultz)
  
  def add_edge(self, x, y):
    self.adjlist[x].append(y)
    self.indegree[y] += 1

  def kahn_sort(self, listofpages):
    queue = []
    for e in listofpages:
      if self.indegree[e] == 0:
        queue.append(e)

    output=[]
    while queue:
      x = queue.pop(0)
      output.append(x)
      for e in self.adjlist[x]:
        self.indegree[e] -= 1
        if self.indegree[e] == 0:
          queue.append(e)
    
    return output


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

  if not rulebroken:
    continue
  rulebroken = False

  edges = rulesforupdate(update)
  fixedupdate = Graph(len(update))
  for x, y in edges:
    fixedupdate.add_edge(x, y)
  fixedupdate = fixedupdate.kahn_sort(update)
  output += fixedupdate[(len(fixedupdate)-1)//2]

print(output)