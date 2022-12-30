
file=open('./input.txt', 'r')

def are_ordered(p1, p2, index):
  #print("."*index*2, p1, "\n", "."*(index*2-1),p2)
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
  result = are_ordered(p1[0], p2[0],index+1)
  if result == 0:
    return are_ordered(p1[1:],p2[1:],index+1)
  return result

def insert_packet(packet):
  global ordered_packets
  print("insert \n{}".format(packet))
  # print("to:")
  # for p in ordered_packets:
  #   print(p)
  if not ordered_packets:
    ordered_packets.append(packet)
    # print("Result:")
    # for p in ordered_packets:
    #     print(p)
    print("---")
    return 1
  p1=list(packet)
  for p_id, p in enumerate(ordered_packets):
    p2=list(p)
    if are_ordered(p1,p2,1) == 1:
      ordered_packets.insert(p_id,packet)
      print("Position", p_id+1)
      #print("Result:")
      # for p in ordered_packets:
      #   print(p)
      #print("---")
      #input()
   #   input()
      return p_id+1      
  ordered_packets.append(packet)
  print("Position at the end", p_id+2)
  #input()
  return p_id+2
      

pair_index = 0
index_sum = 0
ordered_packets=[]
last_one=False
id1=0
id2=0
while True:
  pair_index+=1
  pair1=file.readline().strip()

  if not pair1: 
    id1=insert_packet([[2]])
    print("INDEX:", id1)
    input()
    
    id2=insert_packet([[6]])
    print("INDEX:", id2)
    input()
    
    break
  
  pair1=eval(pair1)
  pair2=eval(file.readline().strip())
  empty=file.readline()
  insert_packet(pair1)
  insert_packet(pair2)

  #input()
file.close()

print("Sum of ordered indexes: ", id1*id2)