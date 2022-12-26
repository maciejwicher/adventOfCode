import os
import time

inputData = "c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/05/input-test.txt"
inputData = "c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/05/input.txt"

crates=[]
def print_crates():
  global crates
  print(type(crates))
  if type(crates) is dict:
    for k in crates:
      print("{}:{}".format(k,crates[k]))
  else:
    for crate in crates:
      print(crate)

file=open(inputData, 'r')

while True:
  line=file.readline()
  if len(line)==1:
    break
  if not crates:
    crates=[[a] for a in list(line[1::4])]    
  else:
    list(map(lambda x,y: x.extend(y),crates,[[a] for a in list(line[1::4])]))
    pass



print("Before reverse:")
print_crates()

list(map(lambda x: x.reverse(), crates))

print("After reverse:")
print_crates()


crates={a.pop(0): list(filter(lambda x: x!=' ', a)) for a in crates}
print_crates()



while True:
  os.system('cls')
#  print_crates()
  line=file.readline()
  if not line:
    break
  q,f,t=list(filter(lambda x: x.isnumeric(), line.split()))
  for i in range(int(q)):
    crate=crates[f].pop()
    crates[t].extend(crate)
  print("Moving {} crates from {} to {}".format(q,f,t))
  #time.sleep(2)
  #input()
  #print(line, q,f,t)
answer="".join([crates[a][:-1] for a in crates ])
print(answer)
file.close()
