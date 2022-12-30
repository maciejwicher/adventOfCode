import re

from ctypes import *
import os

STD_OUTPUT_HANDLE = -11

class COORD(Structure):
    pass
    
COORD._fields_ = [("X", c_short), ("Y", c_short)]

def print_at(r, c, s):
    h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))
    
    c = s.encode("windows-1252")
    windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)

limit=4000000

file=open('./input.txt', 'r')
sensors={}
beacons=[]
pixels={}


while True:
  line=file.readline().strip()
  #print("Examining line", line)
  if not line: break
  cmdResult = re.search(r'Sensor at x=(-?\d+), y=(-?\d+).*is at x=(-?\d+), y=(-?\d+)', line)
  sX, sY, bX, bY = None, None, None, None
  if cmdResult:
    sX,sY,bX,bY = [int(x) for x in cmdResult.groups()]
  #print(line)
  #print(sX,sY,bX,bY)
  #beacons.append((bX,bY))
  sensors[(sX,sY)]=abs(sX-bX)+abs(sY-bY)

verbose=True
def d_print(*message):
  if verbose: print(message)

def get_gap(coverage):  
  #print("Examining:\n{}".format(coverage))
  c=sorted(coverage)
  #print("Sorted version:\n{}".format(c))
  start=0
  end=limit
  x,y=c.pop(0)
  if x>start:
    #print("Mam gap:",start)
    return start

  while c:
    x1,y1=c.pop(0)
    if y < x1-1:
      #print("mam gap:",x1-1)
      return x1-1
    y=max(y,y1)

  if y<end: 
    #print("mam gap:", end)
    return end

  return None
gap=None

for line in range (limit+1):
  if line%10000==0:
    print("Examining line", line, "({}%)".format(round(100*(line+1)/limit, 6)))#, end="")
  coverage=[]
  for x,y in sensors.keys():
    
    radius = sensors[(x,y)]
    distance = abs(line-y)
    #print("Examining",x,y, "with radius", radius, "and distance to line",line,":",distance)
    line_radius=radius-distance
    if line_radius<0:
      #print("This sensor does not reach line",line)
      continue
    x_min= max(x-line_radius,0)
    x_max =min(x+line_radius, limit)
    coverage.append((x_min,x_max))
  gap = get_gap(coverage)
  if gap: 
    print("Beacon found at ({},{})".format(gap, line))
    break
if not gap:
  print("Beacon not found, sorry...")


  
