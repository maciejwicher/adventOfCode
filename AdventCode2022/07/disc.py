import os
import time
import re
from functools import reduce

inputData = "c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/07/input-test.txt"
inputData = "c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/07/input.txt"

file=open(inputData, 'r')

debug=False

current_path=[]
current_directory=""
hdd={"/":0}
while True:
  line=file.readline().strip()
  if not line:
    break
  if debug: print("Line: {}".format(line))
  command = re.search(r'\$ cd (.*)', line)
  if (command):
    directory=command.groups()[0]
    if debug: print("Change directory detected to '{}'".format(directory))
    if directory=="..":
      current_path.pop()
      current_directory=current_path[-1:]
    else:
      if directory=="/": directory=""
      if debug: print("Current path is: {}".format(current_path)) 
      current_directory = ''.join(current_path[-1:])+directory+"/"
      if debug: print("Current directory is: {}".format(current_directory)) 
      current_path.append(current_directory)
      if debug: print("Switched to directory {}".format(current_path))
    
  size = re.search(r'(\d+).*', line)
  if size:
    size = int(size.groups()[0])
    if debug: print("file detected with size {}".format(size))
    size_update = { directory: hdd.get(directory,0)+size for directory in current_path }
    hdd.update(size_update)
    if debug: print("Current update: {}".format(size_update))
    if debug: print("currend hdd state: {}".format(hdd))

  command=None
  size=None

if debug: print(hdd)
small_dirs={k: v for k,v in hdd.items() if v<100000}
if debug: print(small_dirs)
small_sum = reduce(lambda x,y: x+y, filter(lambda x: x<100000, hdd.values()))
print("Sum of directories under 100000: {}".format(small_sum))
free_space=70000000-hdd["/"]
space_needed=30000000-free_space

print("Free space: {}, Space needed: {}".format(free_space, space_needed))

to_delete=min(filter(lambda x: x>space_needed, hdd.values()))
print("Need to delete file with size: {}".format(to_delete))