import re

file=open('./input.txt', 'r')
sensors={}
beacons=[]
while True:
  line=file.readline().strip()
  if not line: break
  cmdResult = re.search(r'Sensor at x=(-?\d+), y=(-?\d+).*is at x=(-?\d+), y=(-?\d+)', line)
  sX, sY, bX, bY = None, None, None, None
  if cmdResult:
    sX,sY,bX,bY = [int(x) for x in cmdResult.groups()]
  #print(line)
  #print(sX,sY,bX,bY)
  beacons.append((bX,bY))
  sensors[(sX,sY)]=abs(sX-bX)+abs(sY-bY)

line=2000000
no_beacons=[]
for x,y in sensors.keys():
  half_wide=sensors[(x,y)]-abs(line-y)
  if half_wide < 0:
    continue
  else:
    r=list(range(x-half_wide, x+half_wide+1))
    no_beacons=list(no_beacons + list(set(r) - set(no_beacons)))
beacons_in_line=[]
for x,y in beacons:
  if line==y: beacons_in_line.append(x)
no_beacons=list(set(no_beacons)-set(beacons_in_line))
print(len(no_beacons))
print(min(no_beacons), max(no_beacons))
#print(sorted(no_beacons))
  
