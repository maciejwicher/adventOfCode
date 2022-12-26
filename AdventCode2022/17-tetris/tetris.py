import functools
import os

inputData = "c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/17-tetris/input-test.txt"

inputData = "c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/17-tetris/input.txt"

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

cave_width=7
total_width=9

def print_cave(cave, width=cave_width):
  i = 1
  width+=2
  while True:
    print(cave[-i*width:][:width].replace("0", " ").replace("1","*"))
    i+=1
    if i*width > len(cave): break

def generate_cave(width):
  #floor
  cave=""
  floor="1" + "1"*width + "1"
  cave+=floor
  for i in range(3):
    cave+="1" + "0"*width + "1"
  #print(cave)
  #print_cave(cave,width)


rocks=["100111101",
        "100010001100111001100010001", 
        "100111001100001001100001001",
        "100100001100100001100100001100100001",
        "100110001100110001"]

rock=rocks[3]
newRock=[[rock,i*total_width,"1"+rock[2+i*total_width:8+i*total_width]+"01"] for i in range(len(rock)//total_width)]
print(rock[11:17])
print(rock)
print(newRock)


newRock="".join(["10"+rock[1+i*total_width:7+i*total_width] + "1" for i in range(len(rock)//total_width)])
print(rock)
print(newRock)
#exit()

#os.system('cls')

#cave=generate_cave(cave_width)

# rock=rocks[3]
# width=cave_width+2
# nRock=""
# for i in range(len(rock)//s):
#   nRock+="1"+rock[2+i*s:8+i*s]+"01"
# shift left
# nRock="".join(["1"+rock[2+i*s:8+i*s]+"01" for i in range(len(rock)//s)])
# # shift right
# nRock="".join(["10"+rock[1+i*s:7+i*s]+"1" for i in range(len(rock)//s)])

# rockPixels=functools.reduce(lambda a,b: int(a)+int(b), rock)
# nRockPixels=functools.reduce(lambda a,b: int(a)+int(b), nRock)
# print("Ilosci pixeli:", rockPixels, nRockPixels)
# while rockPixels == nRockPixels:

#   nRock="".join(["1"+nRock[2+i*s:8+i*s]+"01" for i in range(len(nRock)//s)])
  
#   nRockPixels=functools.reduce(lambda a,b: int(a)+int(b), nRock)
#   print(nRock, nRockPixels)






def count_rock(rock):
  return functools.reduce(lambda a,b: int(a)+int(b), rock)-2*(len(rock)//total_width)

def count_cave(cave):
  return functools.reduce(lambda a,b: int(a)+int(b), cave)

file=open(inputData, 'r')
windMap=file.readline().strip()
windCount=len(windMap)
windIndex=0
cave = "1" + "1"*cave_width + "1"
rock_landed=0
pile_height=0
os.system('cls')

while rock_landed<2022:
  # -- generate next rock
  rock=rocks[rock_landed%len(rocks)]
  rockPixels=count_rock(rock)
  # -- generate cave + empty 3 + height of rock
  cave+="100000001"*(3+len(rock)//total_width)
  cavePixels=count_cave(cave)
  rowOnMap=len(cave)//total_width-len(rock)//total_width
  landed=False
  displayCave=cave

  rockBackground=cave[rowOnMap*total_width:rowOnMap*9+len(rock)]
  wklejka=''.join([str(int(rock[i]) or int(rockBackground[i])) for i in range(len(rockBackground))])
  displayCave=cave[:rowOnMap*total_width]+wklejka+cave[rowOnMap*9+len(rock):]
  # os.system('cls')
  # print("NEW ROCK APPEARED")
  # print_cave(displayCave)
  # input()
  # -- move left or right 3 times (if possible) ----------------------------------------
  while not landed:
    wind=windMap[windIndex%windCount]
    if wind=="<":
      newRock="".join(["1"+rock[2+i*total_width:8+i*total_width]+"01" for i in range(len(rock)//total_width)])
    else:
      newRock="".join(["10"+rock[1+i*total_width:7+i*total_width] + "1" for i in range(len(rock)//total_width)])
    
    newRockPixels=functools.reduce(lambda a,b: int(a)+int(b), newRock)-2*(len(newRock)//total_width)

    rockBackground=cave[rowOnMap*total_width:rowOnMap*9+len(rock)]
    wklejka=''.join([str(int(newRock[i]) or int(rockBackground[i])) for i in range(len(rockBackground))])
    tmpCave=cave[:rowOnMap*total_width]+wklejka+cave[rowOnMap*9+len(newRock):]     
    tmpCavePixels=count_cave(tmpCave)
    # print("\nWind:", wind)
    # input() 
    # os.system('cls')
    # print("TMP CAVE")
    # print_cave(tmpCave)
    # print("tmpCavePixels, cavePixels, rockPixels, newRockPixels", tmpCavePixels, cavePixels, rockPixels, newRockPixels)
    if newRockPixels==rockPixels and tmpCavePixels==(cavePixels+newRockPixels):
      rock=newRock
      displayCave=tmpCave
    else:
      pass
    windIndex+=1
   
    # input()
    
    # os.system('cls')
    # print("CURRENT CAVE")
    # print_cave(displayCave)
    # input()
  # ----------------------------------------------------------------------------  
  # -- print cave + rock

    rowOnMap-=1
    rockBackground=cave[rowOnMap*total_width:rowOnMap*9+len(rock)]
    wklejka=''.join([str(int(rock[i]) or int(rockBackground[i])) for i in range(len(rockBackground))])
    tmpCave=cave[:rowOnMap*total_width]+wklejka+cave[rowOnMap*9+len(rock):]
    #os.system('cls')
    # print("MOVED DOWN CAVE (proposal)")
    # print_cave(tmpCave)
    # input()
    newCavePixels=functools.reduce(lambda a,b: int(a)+int(b), tmpCave)
    if newCavePixels==cavePixels+rockPixels:
      #print("Rock moved down (jupi)                         ")
      displayCave=tmpCave
    else:
      landed=True
      rock_landed+=1
      #cave=displayCave

      cave=''.join(list(filter(lambda x : x!="100000001", (displayCave[i*total_width:total_width*(i+1)] for i in range(len(displayCave)//total_width)))))
      

  print_at(0,0,"rocks landed:{}                     ".format(rock_landed))
  pile_height=len(cave)//total_width-1
  print_at(1,0,"height      :{}                     ".format(pile_height))
    # print("After move down evaluated")
    # print_cave(displayCave)
    # input()
      # print("---------------------")
      #print_cave(tmpCave)
    # -- if not possible to go down - landed
    # ---- rewrite rock to the map
    # - rock = rock + 1

pile_height=len(cave)//total_width-1
print("Wysokosc wiezy:", pile_height)

