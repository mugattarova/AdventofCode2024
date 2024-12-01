import re

f = open("input", "r")
lines = f.readlines()
outSum = 0
firstList = []
secondList = []

for line in lines:
  ints = re.findall('\d+', line)
  
  firstList.append(int(ints[0]))
  secondList.append(int(ints[1]))
    
firstList.sort()
secondList.sort()
outSum=0

while firstList:
  outSum += abs(firstList.pop(0) - secondList.pop(0))

print(outSum)