import re

output=0
with open("input", 'r') as file:
  for line in file:
    matches = re.findall('mul\((\d+),\s*(\d+)\)', line)
    for x, y in matches:
      output+=int(x)*int(y)

print(output)