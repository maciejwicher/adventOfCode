import os

whichDay=input("Ktory dzien?: ")
nickname=input("Nickname puzzla: ")

dirName="{}-{}".format(whichDay,nickname)
os.mkdir(dirName)
files=["{}.py".format(nickname), "input-test.txt", "input.txt"]
for file in files:
  f=open("{}\{}".format(dirName,file), 'w')
  f.close()