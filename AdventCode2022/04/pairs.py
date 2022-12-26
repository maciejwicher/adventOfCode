#inputData = "c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/04/input-test.txt"
inputData = "c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/04/input.txt"

file=open(inputData, 'r')
total=0
while True:
  line=file.readline().strip()
  if not line:
    break
  p1,p2=[[int(b),int(c)] for b,c in [a.split("-") for a in line.split(",")]]
  if p1[0] <= p2[0] and p1[1] >= p2[0]:
    #print("{} {} bo {} <= {} i {} >= {}".format(p1,p2,p1[0],p2[0],p1[1],p2[1]))
    total+=1
  elif p1[0] <= p2[1] and p1[1] >= p2[1]:
    #print("{} {} bo {} <= {} i {} >= {}".format(p1,p2,p2[0],p1[0],p2[1],p1[1]))
    total+=1
  elif p1[0] >= p2[0] and p1[1] <= p2[1]:
    total+=1
  else:
    print(p1,p2)
print("total: {}".format(total))

