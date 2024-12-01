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
cur=0
flCount=0
slCount=0

while firstList:
  if firstList[0]==cur:
    flCount+=1
    firstList.pop(0)
  else:
    slCount = secondList.count(cur)
    outSum += cur*flCount*slCount
    cur=firstList[0]    
    flCount=0
    slCount=0
    
print(outSum)