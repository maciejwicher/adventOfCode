

from ctypes import *
import os

inputData = "c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/10 - signal/input-test.txt"
inputData = "c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/10 - signal/input.txt"


STD_OUTPUT_HANDLE = -11

class COORD(Structure):
    pass
    
COORD._fields_ = [("X", c_short), ("Y", c_short)]

def print_at(r, c, s):
    h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))
    
    c = s.encode("windows-1252")
    windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)

screen_start_row=10
screen_width=40
light_pixel="@"
dark_pixel=" "

    
os.system('cls')
cycle=1
electron=(cycle-1)%screen_width
X=1
print_at(0,0,"Cycle: {}".format(cycle))
print_at(1,0,"Sprite position: {}".format(X))

for i in range(6):
  print_at(screen_start_row+i,42,str(i+1))

file=open(inputData,'r')

loops=1
for line in file:
  if not line:
    break
  line=line.strip()
  print_at(2,0,"Next command: {}                      ".format(line))

  if line=="noop":
    loops=1
    inc=0
  else:
    g,inc=line.split()
    loops=2

  
  
  for i in range(loops):
    print_at(0,0,"Cycle: {}     ".format(cycle))
    print_at(1,0,"Sprite position: {}     ".format(X))
    print_at(3,0,"Electron at: {}    ".format(electron))
    input()
    if X in range(electron-1,electron+2):
      pixel=light_pixel
    else:
      pixel=dark_pixel
    
    print_at(screen_start_row+(cycle-1)//screen_width, electron, pixel)
    cycle+=1
    electron=(cycle-1)%screen_width
    
    
  X+=int(inc)
  
      
file.close()

