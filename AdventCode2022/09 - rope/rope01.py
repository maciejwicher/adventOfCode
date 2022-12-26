inputData = "c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/09 - rope/input-test.txt"
inputData = "c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/09 - rope/input.txt"

#   ...
#   .H.
#   ..T

# 6321 is too small
first i x, second - y
state_machine={
  (0,0):
  (0,1):
  
   0, 1  0, 1->(0,2) -> ( 0, 1)
   0,-1  0,-1->(0,-2) ( 0,-1)
   
   -1, 0  -1, 0 -> (-1, 0)

   -1, 1  -1, 0 -> -1, 1
           0, 1 -> -1, 1
  (-1,1): {(0,1):(-1,2)=>(-1,1)}

  "CC": {"U":["CU",( 0, 0)],"D":["CD",( 0, 0)],"L":["LC",( 0, 0)],"R":["RC",( 0, 0)]},
  "CU": {"U":["CU",( 0, 1)],"D":["CC",( 0, 0)],"L":["LU",( 0, 0)],"R":["RU",( 0, 0)]},
  "CD": {"U":["CC",( 0, 0)],"D":["CD",( 0,-1)],"L":["LD",( 0, 0)],"R":["RD",( 0, 0)]},
  "LC": {"U":["LU",( 0, 0)],"D":["LD",( 0, 0)],"L":["LC",(-1, 0)],"R":["CC",( 0, 0)]},
  "LU": {"U":["CU",(-1, 1)],"D":["LC",( 0, 0)],"L":["LC",(-1, 1)],"R":["CU",( 0, 0)]},
  "LD": {"U":["LC",( 0, 0)],"D":["CD",(-1,-1)],"L":["LC",(-1,-1)],"R":["CD",( 0, 0)]},
  "RC": {"U":["RU",( 0, 0)],"D":["RD",( 0, 0)],"L":["CC",( 0, 0)],"R":["RC",( 1, 0)]},
  "RU": {"U":["CU",( 1, 1)],"D":["RC",( 0, 0)],"L":["CU",( 0, 0)],"R":["RC",( 1, 1)]},
  "RD": {"U":["RC",( 0, 0)],"D":["CD",( 1,-1)],"L":["CD",( 0, 0)],"R":["RC",( 1,-1)]},
}

commands={
  "U":(0,1),
  "D":(0,-1),
  "L":(-1,0),
  "R":(1,0)
}

r=1

file=open(inputData,'r')
fields_visited={}

# Head, Tail
rope=[(0,0),(0,0)]
x=0; y=0
fields_visited[(x,y)]=1
for line in file:
  if not line:
    break
  #print(line)
  command, i=line.strip().split()
  i=int(i)
  for it in range(i):
    #print("State, command", state, command)
    # ri = rope iterator
    move=commands(command)
    for ri in range(len(rope)):
      rope[ri]=tuple(x+y for x,y in zip(rope[ri], move))
      node=rope[ri]
      if abs(node[0]) == 2:
        move=(-node[0]/abs(node[0]),node[1])
      if abs(node[1]) == 2:
        move=(move[0],-node[1]/abs(node[1]))
    
    #print("New state, mod", state, mod)
    
    #print("x,y before", x, y)
    x+=dx;y+=dy
    #print("x, y after", x, y)
    #print(fields_visited)
    fields_visited["{},{}".format(x,y)]=1
    #print(fields_visited)
    #input()
print("Ogon odwiedzil: ", len(fields_visited.keys()))