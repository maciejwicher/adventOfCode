
file=open('./input.txt', 'r')

def are_ordered(p1, p2, index):
  print("."*index*2, p1, "\n", "."*(index*2-1),p2)
  is_p1_list = type(p1) is list
  is_p2_list = type(p2) is list
  if is_p1_list != is_p2_list:
    if is_p1_list:
      return are_ordered(p1,[p2],index+1)
    else:
      return are_ordered([p1],p2,index+1)
  if not is_p1_list:
    if p1 < p2: return 1
    if p1 > p2: return -1
    return 0
  if not p1 and not p2: return 0
  if not p1: return 1
  if not p2: return -1
  result = are_ordered(p1.pop(0), p2.pop(0),index+1)
  if result == 0:
    return are_ordered(p1,p2,index+1)
  return result

pair_index = 0
index_sum = 0
while True:
  pair_index+=1
  pair1=file.readline().strip()
  if not pair1:
    break
  pair1=eval(pair1)
  pair2=eval(file.readline().strip())
  empty=file.readline()
  #print(pair1, pair2)
  print("Checking pair {}: \n{}\n{}".format(pair_index, pair1, pair2))
  if are_ordered(pair1, pair2,1) == 1:
    index_sum+=pair_index
    print("...They are ordered. Sum of index is:", index_sum)
  else:
    print("...They are not ordered. Sorry...")
  #input()
file.close()

print("Sum of ordered indexes: ", index_sum)