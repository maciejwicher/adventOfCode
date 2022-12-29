
file=open('./test-input.txt', 'r')

while True:
  pair1=eval(file.readline().strip())
  pair2=eval(file.readline().strip())
  empty=file.readline()
  if not pair1:
    break
  print(pair1, pair2)

file.close()