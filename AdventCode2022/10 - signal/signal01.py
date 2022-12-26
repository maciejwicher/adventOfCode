
inputData = "c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/10 - signal/input-test.txt"

inputData = "c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/10 - signal/input.txt"

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


os.system('cls')
cycle=1
X=1
cycle=1
print_at(0,0,"Cycle: {}".format(cycle))
print_at(0,1,"Sprite position: {}".format(X))

file=open(inputData,'r')

catchPoints=[20,60,100,140,180,220]
currentCatchPoint=catchPoints.pop(0)
signalStrength=0
for line in file:
  if not line:
    break

  line=line.strip()
  print("'{}'".format(line))
  print(len(line))
  commandEnd=False
  if cycle==currentCatchPoint:
    signalStrength+=(X*currentCatchPoint)
    if not catchPoints: break
    currentCatchPoint=catchPoints.pop(0)
  if line=="noop":
    print("noop detected")
    cycle+=1
  else:
    print("command detected")
    # it means, that command will pass through a checkpoint
    if cycle==currentCatchPoint-1:
      signalStrength+=(X*currentCatchPoint)
      if not catchPoints: break
      currentCatchPoint=catchPoints.pop(0)
    g,inc=line.split()
    cycle+=2
    X+=int(inc)  
file.close()
print("Signal strength is ", signalStrength)
