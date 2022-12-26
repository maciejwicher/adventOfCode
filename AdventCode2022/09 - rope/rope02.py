#inputData = "c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/09 - rope/input-test.txt"
#inputData = "c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/09 - rope/input-test2.txt"
inputData = "c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/09 - rope/input.txt"

from ctypes import *

STD_OUTPUT_HANDLE = -11

class COORD(Structure):
    pass
    
COORD._fields_ = [("X", c_short), ("Y", c_short)]

def print_at(r, c, s):
    h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))
    
    c = s.encode("windows-1252")
    windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)




#   ...
#   .H.
#   ..T

# 6321 is too small


commands={
  "U":(0,1),
  "D":(0,-1),
  "L":(-1,0),
  "R":(1,0)
}

r=1

file=open(inputData,'r')
begin=(0,0)
minimum=(0,0)
maximum=(0,0)
for line in file:
 # print(line)
  command, it = line.strip().split()
  cmd=commands[command]
  
  begin=tuple([x*int(it)+y for x,y in zip(cmd,begin)])
  minimum=tuple([min(x,y) for x,y in zip(minimum,begin)])
  maximum=tuple([max(x,y) for x,y in zip(maximum,begin)])
  
file.close()
print(begin, minimum, maximum)

file=open(inputData,'r')

fields_visited={}

# Head, Tail
rope=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
x=0; y=0
fields_visited[(x,y)]=1
for line in file:
  if not line:
    break
  #print("***************", line.strip())
  command, i=line.strip().split()
  i=int(i)
  for it in range(i):
    #print("command", command, it, line.strip())
    # ri = rope iterator
    move=commands[command]
    #print("Move is:", move)
    for ri in range(len(rope)):
      #print("rusza ",ri)
      #print("before:", rope[ri])
      rope[ri]=tuple(x+y for x,y in zip(rope[ri], move))
      #print("after:", rope[ri])
      nx,ny=rope[ri]
      move=(0,0)
      # (2,2)
      if abs(nx) == 2 and abs(ny) == 2:
        move=(nx//abs(nx),ny//abs(ny))
        rope[ri]=tuple([x-y for x,y in zip(rope[ri],move)])
      elif abs(nx) == 2:
        # (1,2)
        move=(nx//abs(nx),ny)
        #print("first move,nodere",move,node[ri])
        # rope[ri]==1,0
        rope[ri]=tuple([x-y for x,y in zip(rope[ri],move)])
      elif abs(ny) == 2:
        move=(nx,ny//abs(ny))
        #print("second move,nodere",move,node[ri])     
        rope[ri]=tuple([x-y for x,y in zip(rope[ri],move)])
      if move == (0,0):
        break
      #print("next piece move:", move)
    ##print("New state, mod", state, mod)
    #print("Cala lina po ruchu", rope)
    #print("ogon ma ruszyc o: ", move)
    ##print("x,y before", x, y)
    #x+=dx;y+=dy
    ##print("x, y after", x, y)
    ##print(fields_visited)
    # print("Tailcoords")
    tail_coords=tuple([a+b for a,b in zip(rope[-1],[x,y])])
    
    #print("Koordynaty ogona:", tail_coords)
    fields_visited[tail_coords]=1
    #print("Odwiedzone pola", fields_visited)
    x,y = tail_coords
    rope[-1]=(0,0)

    #print("Ogon zwizytowal:",fields_visited)
    #input()
    # 2358 - too small
    # 2643 - this is it :)
print("Ogon odwiedzil: ", len(fields_visited.keys()))