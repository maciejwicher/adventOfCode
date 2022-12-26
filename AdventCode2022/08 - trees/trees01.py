import os
import time
from functools import reduce
import operator

inputData = "c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/08 - trees/input-test.txt"
#inputData = "c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/08 - trees/input.txt"
theMap=[]
colA=[]
colB=[]
rowA=[]
rowB=[]

def printMap(theMap):
  for y in range(len(theMap[0])):
    for x in range(len(theMap)):
      print(theMap[x][y], end=" ")
    print()
    
def eliminate_invisibles(theMap):
  print("Elimiating {}".format(theMap))
  x=0
  for segment in theMap:
    visible=0
    y=0
    for tree in segment:
      if tree>visible:
        visible=tree
        theMap[x][y]=1
      else:
        theMap[x][y]=0
      y+=1
    x+=1
  print("Eliminated {}".format(theMap))
    


file=open(inputData, 'r')
while True:
  line=file.readline().strip()
  if not line:
    break
  if (not colA):
    colA=[list([]) for char in line]
  x=0
  for char in line:
    colA[x].append(int(char)+1)
    x+=1
  rowA.append([int(c)+1 for c in line])

theMap=list(colA)
print("Mapa z kolumn")
printMap(theMap)
print("Mapa z wierszy")
for r in rowA: print(r)

colB=[x[::-1] for x in colA]
rowB=[x[::-1] for x in rowA]
print(colA)
print(colB)
print(rowA)
print(rowB)

print()

eliminate_invisibles(colA)
eliminate_invisibles(colB)
eliminate_invisibles(rowA)
eliminate_invisibles(rowB)

print("Pszekształcenia")
print("colB before:{}".format(colB))
colB=[x[::-1] for x in colB]
print("colB after: {}".format(colB))
print("colA to   : {}".format(colA))
col=[[x or y for x,y in zip(a,b)] for a,b in zip(colA,colB)]
print("COLS JOINED")
printMap(col)
rowB=[x[::-1] for x in rowB]
print("ROW A{}\nROW B{}".format(rowA, rowB))
row=[[x or y for x,y in zip(a,b)] for a,b in zip(rowA,rowB)]
print("ROWS JOINED")
for r in row: print(r)
col_transformed=[list([]) for e in col]
for c in col:
  x=0
  for tree in c:
    col_transformed[x].append(tree)
    x+=1
print(col)
print(col_transformed)
final=[[x or y for x,y in zip(a,b)] for a,b in zip(row,col_transformed)]
for f in final: print(f)
#os.system("cls")
#print("Join        {}".format(col))
#row=[(x or y) for x,y in zip(rowA,[x[::-1] for x in rowB])]
#print("Row:{}\nCol:{}".format(row,col))
#printMap(col)

result = reduce(operator.add,[x for row in final for x in row])
print(result)
#os.system("cls")
# print("ZIP TEST")
# print(colB)
# print(colA)
# print("IIIIIINNY TESTTTTTT")
# print(["{},{}".format(x,y) for x,y in zip(colA,colB)])
# print(list(zip(colA,colB)))


a=[[1,2,3], [4,5,6]]
for s in a:
  print(s)
  s[1]="X"

print(a)