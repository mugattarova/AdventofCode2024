import numpy as np

inp = []
with open("input", 'r') as file:
  for line in file:
    matches = list(line.strip())
    inp = list(map(int, matches))
  
diskmap = []
numbers = dict()
spaces = dict()
for i in range(len(inp)):
  if i%2==0:
    elem = i//2
    #        number    start_ind     len
    numbers[i//2] = [len(diskmap), inp[i]]

    #        start_ind        len   number
    # numbers[len(diskmap)] = [inp[i], i//2]
  else:
    elem = None
    if inp[i] > 0:
      #       start_ind       len
      spaces[len(diskmap)] = inp[i]

  for j in range(inp[i]):
    diskmap.append(elem)


sorted_spaces = sorted(spaces.keys())
backnum = diskmap[-1]
file_ind = numbers[backnum][0]
file_len = numbers[backnum][1]
while not (file_ind < sorted_spaces[0]):
  if file_len <= max(spaces.values()):
    for i in range(len(sorted_spaces)):

      # space found
      if (file_len <= spaces[sorted_spaces[i]]) and (file_ind > sorted_spaces[i]):
        for j in range(file_len):
          diskmap[sorted_spaces[i]+j] = backnum

        # empty previous backnum block
        for j in range(file_len):
          diskmap[file_ind+j] = None
        
        # adjust spaces array
        if file_len < spaces[sorted_spaces[i]]:
          spaces[sorted_spaces[i] + file_len] = spaces[sorted_spaces[i]] - file_len
        del spaces[sorted_spaces[i]]
        break


  # last
  sorted_spaces = sorted(spaces.keys())
  del numbers[backnum]
  backnum -= 1
  file_ind = numbers[backnum][0]
  file_len = numbers[backnum][1]
  if backnum < 0:
    break



for i in range(len(diskmap)):
  if diskmap[i] is None:
    diskmap[i] = 0

output = sum(map(lambda x: x[0]*x[1], enumerate(diskmap)))
print(output)
# print(''.join(map(str, diskmap)))