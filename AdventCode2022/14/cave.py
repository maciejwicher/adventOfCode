import os
import time
from ctypes import *

STD_OUTPUT_HANDLE = -11

class COORD(Structure):
    pass
    
COORD._fields_ = [("X", c_short), ("Y", c_short)]

air=" "
sand="."
def print_at(r, c, s):
    col=2*r
    row=c+5
    c=col
    r=row
    #print_at(2,sandDrops*2, "o")
    h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))
    
    c = s.encode("windows-1252")
    windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)



inputData = "c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/14/cave-test.txt"
inputData = "c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/14/cave.txt"

file=open(inputData, 'r')

rock_data=[]
cave_data=[]
maxX=500
maxX_y=0
minX=500
minX_y=0

maxY=0
minY=0
cave=[]

def print_cave():
  for y in range(height):
    for x in range(width):
      #print("x {} y {}".format(x,y), end="")
      print(cave[x][y], end=" ")
    print()


while True:
  line=file.readline().strip()
  if not line:
    break
  rock_data.append(line)
  coords=line.split(" -> ")
  #print(line)
  #print("Received coords: {}".format(coords))
  for coord in coords:
    #print("Examining coordinate: {}".format(coord))
    x, y = [int(x) for x in (coord.split(","))]
    #print("x is {} and y is {}".format(x,y))
    if x > maxX:
      maxX=x
      maxX_y=y
    elif x < minX:
      minX=x
      minX_y=y
    if y > maxY:
      maxY=y
  #print("X:{}-{}, Y:{}-{}".format(minX,maxX,minY,maxY))
  width=maxX-minX+1
  height=maxY+1+2
  sandDrops=500-minX

right_margin = height-maxX_y-1+4+200
left_margin = height-minX_y-1+4+200
sandDrops=sandDrops #+left_margin
#width=width #+left_margin #+right_margin

print("Najbardziej na prawo punkt to {}x{}".format(maxX,maxX_y))
print("Najbardziej na lewo punkt to {}x{}".format(minX,minX_y))
print()
  
  #print("Cave is {}x{}".format(width,height))

def create_matrix(x,y):
  print("***creating cave {}x{}".format(x,y))
  matrix=[list(air for c in range(y)) for b in range(x)]
#  print("Created matrix: {}".format(matrix))
  return matrix  
# Create cave:

cave=create_matrix(width, height)
# for y in range(height-1):
#   for x in range(width-1):
#     #print("x {} y {}".format(x,y), end="")
#     print(cave[x][y], end=" ")
#   print()

def print_line(px, py, x, y):
  global cave
  #print("Printing line [{},{}]-->[{},{}]".format(px,py,x,y))
  if px == x:
    #print("Iksy te same")
    dy=1
    if py > y: dy = -1
    #print("py {} y {} dy {} x {}". format(py, y, dy, x))
    for myY in range(py, y+dy, dy):
      cave[x][myY]="#"
  else:
    dx=1
    if px > x: dx = -1
    for myX in range(px, x+dx, dx):
      cave[myX][y]="#"
  #print_cave()





for rock in rock_data:
  prev_x=None
  prev_y=None
  coords=rock.split(" -> ")
  #print(rock)
  #print("Received coords: {}".format(coords))
  for coord in coords:
    #print("Examining coordinate: {}".format(coord))
    x, y = [int(x) for x in (coord.split(","))]
    x=x-minX #+left_margin
    #print("x is {} and y is {}".format(x,y))
    if prev_x is None:
      prev_x=x
      prev_y=y
      #print("skipping first record")
      continue
    print_line(prev_x,prev_y, x,y)
    prev_x=x
    prev_y=y
print_line(0,height-1,width-1,height-1)
cave[sandDrops][0]=sand
print("")
print_cave()

file.close()

nextSand=False
x=sandDrops
y=0
print_at(sandDrops, 0, sand)
sandQuantity=0
while True:
  #print_at(1,height+3, "Sand in cave: {}".format(sandQuantity))
  #move down
  if y==height-1:
    #print_at(13,13, "{} {}koniec           ".format(x,y))
    print_at(x,y,air)
    break
  elif y==height-2 and (x==0 or x==width):
    #print_at(13,13, "{} {}koniec           ".format(x,y))
    print_at(x,y,air)
    break
  elif cave[x][y+1]==air:
    #print_at(13,13, "{} {}w dol!           ".format(x,y))
    dx=x; dy=y+1
  elif x == 0:
    #print_at(13,13, "{} {}koniec           ".format(x,y))
    print_at(x,y,air)
    break
  elif cave[x-1][y+1]==air:
    #print_at(13,13, "{} {}w lewo!           ".format(x,y))
    dx=x-1; dy=y+1
  elif x==width-1:
    #print_at(13,13, "{} {}koniec           ".format(x,y))
    print_at(x,y,air)
    break
  elif cave[x+1][y+1]==air:
    #print_at(13,13, "{} {}w prawo !           ".format(x,y))
    dx=x+1; dy=y+1
  elif y==0:
    sandQuantity+=1
    break
  else:
    #print_at(13,13, "{} {}next sand         ".format(x,y))
    nextSand=True


  if nextSand:
    nextSand=False
    x=sandDrops
    y=0
    cave[x][y]=sand
    print_at(x,y,sand)
    sandQuantity+=1
    continue
  #time.sleep(0.1)
  #input()
  cave[x][y]=air
  print_at(x,y,air)
  cave[dx][dy]=sand
  print_at(dx,dy,sand)
  x=dx; y=dy

print_at(0,height+3, "Sand in cave: {}".format(sandQuantity))
print_at(0,height+4, "koniec")