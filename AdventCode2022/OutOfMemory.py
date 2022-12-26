import re


file1 = open('./ConsoleData.txt', 'r')
lineNumber = 0

# { [ { "/": { "size": 0, "content" : { 
#   "dirA": { "size": 0, "content": {
#     }},
#   134,
#   234,
#   ""}}}
print("Welcome")
directoryStructure = { [ { "/": { "content" : {}, "size": 0,  } } ] }
directoryLevel1 = { "dirA": {}, "dirB": {}, }
currentDirectory = directoryStructure
parrentDirectory = directoryStructure
# alfa, bet = [ "a", "b"]
# print("alfa: {}, bet {}".format(alfa, bet))
# exit()

while True:
    lineNumber += 1

    # Get next line from file
    line = file1.readline().strip()
    print("Line {} is: '{}'".format(lineNumber,line))

    # Check if thats a command?
    cmdResult = re.search(r'\$\s+(\S+)(\s+(\S+))?', line)
    if cmdResult:
      command,garbage,directory = cmdResult.groups()
      print("Matching command: \"{}\" with arg: \"{}\"".format(command,directory))
      match command:
        case "cd":
          print("--Changing directory to {}".format(cmdResult.group(3)))
          if directory == "..":
            currentDirectory=parrentDirectory
          else:  
            currentDirectory=currentDirectory[directory]
        case "ls":
          print("--Reading content of directory: ")
        

    # else: 
    #   print("String '{}' does not match regexp!".format(line))
    # if lineNumber >=10:
    #   break
    # # if line is empty
    # end of file is reached
    if not line:
        break
    #print("Line {}: {}".format(lineNumber, line.strip()))
  
file1.close()