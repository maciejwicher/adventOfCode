file1 = open("c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/03/Rucksack.txt", 'r')

result=0
error=''
while True:
    line = file1.readline().strip()
    if not line:
      break
    r1=line[:len(line)//2]
    r2=line[len(line)//2:]
    print("{} contains:".format(line))
    print(r1)
    print(r2)
    
    for ch in r1:
      if ch in r2:
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
file1.close()
print("Twoj wynik to: {}".format(result))