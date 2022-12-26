import os
import time

inputData = "c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/12/map.txt"

height=None
width=None
distance=0
startingPoints=[]
newStartingPoints=[]
goalReached=False
space=2

def explore_point(x,y, myHeight):
  global newStartingPoints
  global theMap
  global distance
  global width
  global goalReached
  global height
  #print("Exploring point {},{}".format(x,y), end="")
  if (x>=0 and x<width and y>=0 and y<height):
    markedPoint = theMap[x][y]
    if markedPoint.distance is None and markedPoint.height >= myHeight-1:
      markedPoint.distance = distance
      newStartingPoints.append((x,y))
      #print("...Marked!")
      if markedPoint.letter == "a" or markedPoint.letter=="S":
        #print("...Target reached!!!!")
        goalReached=True
    #else:
      #print("...Visited or too low!")
  #else:
    #print("...Out of the map!")
  return None

def elegant_print(char):
  print('{0: >3}'.format(char), end="")

class GridField:
  letter=None
  height=None
  distance=None
  def __init__(self,letter):
    self.letter=letter
    self.height=ord(self.letter)-96



file=open(inputData, 'r')

theMap=[]
start=None
end=None
x=0
y=0
while True:
  line=file.readline().strip()
  if not line:
    break
  print(line)
  # first row
  if (not theMap):
    theMap=[list([]) for char in line]
  
  for char in line:
    theMap[x].append(GridField(char))
    if char=="S":
      start=(x,y)
      theMap[x][y].height=1
    if char=="E":
      end=(x,y)  
      theMap[x][y].height=26
    x+=1
  x=0
  y+=1

height=len(theMap[0])
width=len(theMap)
print("My map is {}x{}".format(width, height))
print("Start is {}, end is {}".format(start,end))

startingPoints=[(end[0],end[1])]
theMap[end[0]][end[1]].distance=0
distance=1
print("Starting points are {}".format(startingPoints))
goalReached=False
while not goalReached:
  for point in startingPoints:
    #print("-----Exploring from {},{}, height {}".format(point[0],point[1],theMap[point[0]][point[1]].letter))
    myHeight=theMap[point[0]][point[1]].height
    explore_point(point[0]-1,point[1], myHeight)
    explore_point(point[0],point[1]+1, myHeight)
    explore_point(point[0]+1,point[1], myHeight)
    explore_point(point[0],point[1]-1, myHeight)
  distance+=1
  startingPoints=newStartingPoints[:]
  newStartingPoints=[]
  time.sleep(0.01)
  os.system('cls')
  for y in range(height):
    for x in range(width):
      if theMap[x][y].letter == "E":
        elegant_print("E")
      elif theMap[x][y].letter == "S":
        elegant_print("S")
      elif theMap[x][y].distance is None:
        elegant_print(theMap[x][y].letter)
      else:
        elegant_print(theMap[x][y].distance)
    print()
  print("*"*width*3)
  print("****** DISTANCE: {} ******".format(distance-1))
print("Odleglosc to {}".format(distance-1))
  