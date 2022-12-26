import yaml
import re

inputData = "c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/11/monkeys.txt"
outputData = "c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/11/monkeys-fixed.txt"

monkeys = {}
inspections = {}
def fix_yaml():
  file=open(inputData, 'r')
  outFile=open(outputData, 'w')
  endIsComing=False
  while True:
    line=file.readline()
    if not line and endIsComing:
      break
    if not line:
      #print("End is coming!")
      endIsComing=True
      continue
    endIsComing=False
    test = re.search(r'Test: divisible by (.*)', line)
    ifCondition = re.search(r'(If .*): throw to (.*)', line)
    operation = re.search(r'Operation: new = (.*)', line)
    #expression = re.search(r'Expression: divisible by (.*)')
    #monkey = re.search(r'Monkey.*', line)
    if test:
      expression=test.groups()[0]
      #print("Result {}".format(expression))
      outFile.write("  Test:\n")
      outFile.write("    Expression: old % {}\n".format(expression))
    #elif monkey:
     # print(monkey)
      #outFile.write("{}\n".format(monkey.group().lower()))
    elif ifCondition:
      expr=ifCondition.groups()[0]
      monkey=ifCondition.groups()[1]
      outFile.write("    {}: {}\n".format(expr,monkey.capitalize()))
    elif operation:
      op=operation.groups()[0]
      outFile.write("  Operation: {}\n".format(op))
    else:
      outFile.write("{}".format(line))
  print("OK")
  file.close()
  outFile.close()

# structure of the single monkey:
# { "0": { "items": [ x, y, z], }}
my_monkeys={}

def create_monkeys():
  file=open(outputData, 'r')
  global monkeys 
  monkeys = yaml.safe_load(file)
  for monkey in monkeys:
    if isinstance(monkeys[monkey]["Starting items"], int):
      monkeys[monkey]["Starting items"]=[monkeys[monkey]["Starting items"],]
    else:
      monkeys[monkey]["Starting items"]=list(map(int, monkeys[monkey]["Starting items"].split(', ')))
    print("{}: {}".format(monkey,monkeys[monkey]))
    #print(monkey["Starting items"])
    #print("{}:\n  {}\n".format(monkey,monkeys[monkey]))
    
  return
greatDivisor=3*13*5*19*11*7*17*2
def run_simulation():
  Round = 1
  for monkey in monkeys:
      print("{}: {}".format(monkey,monkeys[monkey]["Starting items"]))
      inspections[monkey]=0
  while Round < 10001:
    #print("*********************************************")
    print("****************** Round {}".format(Round))
    #print("*********************************************")
    for monkey in monkeys:
      #print("{}".format(monkey))
      while monkeys[monkey]["Starting items"]:
        #print("    Items are: {}".format(monkeys[monkey]["Starting items"]))
        item = monkeys[monkey]["Starting items"].pop(0)
        
        #print("  Monkey inspects an item with a worry level of {}.".format(item))
        inspections[monkey]+=1

        old = item
        item = eval(monkeys[monkey]["Operation"])
        #print("  Worry level is {} to {}".format(monkeys[monkey]["Operation"], item))
        #item//=3
        #print("  Monkey gets bored with item. Worry level is divided by 3 to {}.".format(item))
        old = item
        isDivisible = eval(monkeys[monkey]["Test"]["Expression"])
        if isDivisible:
          #print("  Is not divisible by {}".format(monkeys[monkey]["Test"]["Expression"]))
          nextMonkey=monkeys[monkey]["Test"]["If false"]
        else:
          #print("  Is divisible by {}".format(monkeys[monkey]["Test"]["Expression"]))
          nextMonkey=monkeys[monkey]["Test"]["If true"]  
        item = item%greatDivisor
        
        monkeys[nextMonkey]["Starting items"].append(item)
      
        #print("  Item with worry level {} is thrown to {}.".format(item,nextMonkey))
    
    for monkey in monkeys:
      print("{}: {}".format(monkey,monkeys[monkey]["Starting items"]))
    Round+=1

    print(inspections)

    monkey1=0
    monkey2=0
    for monkey in inspections:
      if inspections[monkey] > monkey1:
        monkey2 = monkey1
        monkey1=inspections[monkey]
      elif inspections[monkey] > monkey2:
        monkey2=inspections[monkey]

    print("Monkey business is {}*{}={}".format(monkey1,monkey2,monkey1*monkey2))
  return


fix_yaml()
print("Monkeys before:".format(monkeys))
create_monkeys()
print("Monkeys after:".format(monkeys))
run_simulation()
