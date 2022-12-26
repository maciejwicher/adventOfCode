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


def count_rock(rock):
  return functools.reduce(lambda a,b: int(a)+int(b), rock)-2*(len(rock)//total_width)

def count_cave(cave):
  return functools.reduce(lambda a,b: int(a)+int(b), cave)

super_key=None
cycle_mode=False
cycle_finder={}
file=open(inputData, 'r')
windMap=file.readline().strip()
windCount=len(windMap)

windIndex=0
cave = "1" + "1"*cave_width + "1"
rock_landed=0
pile_height=0
os.system('cls')
current_height=0
removed_height=0
rock_limit=2022
rock_limit=1000000000000

while rock_landed<rock_limit:
  rock=rocks[rock_landed%len(rocks)]
  rockPixels=count_rock(rock)
  cave+="100000001"*(3+len(rock)//total_width)
  cavePixels=count_cave(cave)
  rowOnMap=len(cave)//total_width-len(rock)//total_width
  landed=False
  displayCave=cave

  rockBackground=cave[rowOnMap*total_width:rowOnMap*9+len(rock)]
  wklejka=''.join([str(int(rock[i]) or int(rockBackground[i])) for i in range(len(rockBackground))])
  displayCave=cave[:rowOnMap*total_width]+wklejka+cave[rowOnMap*9+len(rock):]
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
    if newRockPixels==rockPixels and tmpCavePixels==(cavePixels+newRockPixels):
      rock=newRock
      displayCave=tmpCave
    else:
      pass
    windIndex+=1

    rowOnMap-=1
    rockBackground=cave[rowOnMap*total_width:rowOnMap*9+len(rock)]
    wklejka=''.join([str(int(rock[i]) or int(rockBackground[i])) for i in range(len(rockBackground))])
    tmpCave=cave[:rowOnMap*total_width]+wklejka+cave[rowOnMap*9+len(rock):]
    newCavePixels=functools.reduce(lambda a,b: int(a)+int(b), tmpCave)
    if newCavePixels==cavePixels+rockPixels:
      displayCave=tmpCave
    else:
      landed=True
      rock_landed+=1



      cave=''.join(list(filter(lambda x : x!="100000001", (displayCave[i*total_width:total_width*(i+1)] for i in range(len(displayCave)//total_width)))))


      matrix="0000000"
      for i in range(len(cave)//total_width-1):
        chunk=cave[-(i+1)*total_width:][1:total_width-1]
        matrix=''.join([str(int(a) or int(b)) for a,b in zip(chunk,matrix)])
        if matrix=="1111111":
          removed_height+=len(cave[:-i*total_width])//total_width-1
          cave="111111111"+cave[-(i)*total_width:]
          
          break
      
      current_height=removed_height+len(cave)//total_width-1
      
      key=str(int(cave,2))
      value=(rock_landed%len(rocks),windIndex%windCount)
      cycle_finder[key]=cycle_finder.get(key,{})
      if cycle_finder[key] and not cycle_mode:
        print("juz byl")
          
        if value in cycle_finder[key]["c"]:
          cycle_mode=True
        cycle_finder[key]["c"].append(value)
        cycle_finder[key]["d"].append((rock_landed, current_height))
        if cycle_mode:
          print("got cycle! After {} rocks, height {}".format(rock_landed, current_height))
          print(cycle_finder[key])
          print("------------------")
          cRocks=cycle_finder[key]["d"][1][0]-cycle_finder[key]["d"][0][0]
          cHeight=cycle_finder[key]["d"][1][1]-cycle_finder[key]["d"][0][1]
          
          rocks_before_cycle=cycle_finder[key]["d"][1][0]
          
          print("rocks, height {} {}".format(cRocks, cHeight))
         
          
          #input()
          #dd=2022
          dd=1000000000000
          cycles_needed=(dd-rocks_before_cycle)//cRocks
          cycles_height=cycles_needed*cHeight
          rocks_left=dd-cycles_needed*cRocks-rocks_before_cycle
          print("mam {} cykli, potrzebuje {} zasymulowac".format(cycles_needed, rocks_left))
          rock_limit=rock_landed+rocks_left
          removed_height+=cycles_height
          

      else:
        print("pirszy raz")
        cycle_finder[key]["c"]=[(value)]
        cycle_finder[key]["d"]=[(rock_landed, current_height)]
        print(cycle_finder[key])
  
      
  print_at(0,0,'')
  print("rocks landed:{}                     ".format(rock_landed))
  print("height      :{}                     ".format(current_height))
  print("ile rockslim:{}     ".format(rock_limit))
  #input()



#os.system('cls')
print_cave(cave)
print("Wysokosc wiezy:\n", current_height)

