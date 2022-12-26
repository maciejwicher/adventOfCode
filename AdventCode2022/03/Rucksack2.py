file1 = open("c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/03/Rucksack.txt", 'r')

result=0
error=''
count=0
lines=[]
while True:
    count+=1
    line=file1.readline().strip()
    print(line)
    lines.append(line)
    if not line:
      break
    if count==3:
      for ch in lines[0]:
        if ch in lines[1] and ch in lines[2]:
          error=ch
          break
      
      value=ord(ch)
      if value >= 97:
        value-=96
      else:
        value=value-65+27
      result+=value
      print("Common letter is: '{}' of value {}. Result is {}".format(ch, value, result))
      print("*********")
      count=0
      lines=[]

file1.close()
print("Twoj wynik to: {}".format(result))