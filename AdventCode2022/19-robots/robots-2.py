from enum import Enum
import math

file=open('.\input-test.txt', 'r')
Mats = Enum('Mats', ['ore', 'clay', 'obsidian', 'geode'])
Robots = Enum('Robot', ['ore', 'clay', 'obsidian', 'geode'])

verbose = True
def collect():
  global storage
  storage=[x+y for x,y in zip(robots,storage)]
  if verbose:
    for i,r in enumerate(robots):
      if verbose: print("{} produced {} {}. You have {}".format(Robots(i+1), robots[i], Mats(i+1), storage[i]))

def can_produce(robot):
  max_prod=10000
  robot_cost=blueprint[robot]
  if verbose: print("Determine if I can buy {} which cost {} with {}".format(robot, robot_cost,storage), end="")
  for idr, resource in enumerate(storage):
    if robot_cost[idr]:
      prod=storage[idr]//robot_cost[idr]
      max_prod=min(prod, max_prod)
  if max_prod:
    if verbose: print("...YES")
  else:
    if verbose: print("...NO")
  return max_prod

def start_production(robot):
  global robot_in_production
  for idr, res in enumerate(blueprint[robot]):
    storage[idr]-=res
  if verbose: print("Spend {} on {}. Left: {}".format(blueprint[robot], robot, storage))
  robot_in_production=robot

def finish_production():
  global robot_in_production
  robots[robot_in_production.value-1]+=1
  if verbose: print("Finished production of {}. You have {}".format(robot_in_production,robots[robot_in_production.value-1]))
  robot_in_production=None

def when_produce(robot):
  cost=blueprint[robot]
  distance = 0
  for idr, resource in enumerate(cost):
    if verbose: print("checking {}...".format(Mats(idr+1)))
    if not resource: 
      if verbose: print("{} not needed to produce {}".format(Mats(idr+1), robot))
      continue
    if storage[idr]>=resource: 
      distance=max(0, distance)
      if verbose: print("We have enough {} to buy {}".format(Mats(idr+1),robot))
    elif robots[idr]==0 : distance=-1;break
    else: 
      distance = max((resource - storage[idr])//robots[idr],distance) 
      if verbose: print("Considering {} we need {} turns to produce {}".format(Mats(idr+1), distance, robot))
  if distance==-1:
    if verbose: print("We do not produce {}. Need to buy {}".format(Mats(idr+1), Robots(idr+1)))
  return distance, Robots(idr+1)
  
blueprints = { 1: { Robots(1): [2,0,0,0], Robots(2): [3,0,0,0], Robots(3): [3,8,0,0], Robots(4): [3,0,12,0]}}

# first - need to produce at least 1 clay, than at least 1 obsidian, than at least 1 geode
# fastest track to r.geode:
# -- fastest track to r.obsidian
# ---- fastest track to clay: wait for ores or build r.ore?
# ------- r.clay can be build in turn: (c.clay[ore]-ores)//r.ore
# ------- r.ore can be build in turn: (c.ore[ore]-ores)//r.ore
# ------- r.clay, if r.ore+1 after t, can be build in turn:  

def simulate_resources(resource):
  return storage[resource.value-1]+robots[resource.value-1]*tLeft
def simulate_resources_with_produced(resource, robot):
  cost=blueprint[robot]
  storageP=list(storage)
  storageP[resource.value-1]-=cost[resource.value-1]
  return storageP[resource.value-1]+robots[robot.value-1]*tLeft+(tLeft-1)

def simulate_production_ability(robot, produced_robot):
  lstorage=list(storage)
  lcost=blueprint[robot]
  diff=[x-y for x,y in zip(lcost,lstorage)]
  print("I want to create {} for {}. Have {}. Missing: {}".format(robot,lcost,lstorage,diff))
  
  if produced_robot:
    print("I want to be smart and produce {} to help me".format(produced_robot))
    lstorage=[x-y for x,y in zip(lstorage,blueprint[produced_robot])]
    when=[ -1 if speed==0 else math.ceil(1+(goal-speed)/(speed+1)) for goal,speed in zip(diff,robots)]
  else:
    when=[ -1 if speed==0 else math.ceil(goal/speed) for goal,speed in zip(diff,robots)]
  print("When matrix: ", when)
  when = max(when)
  print("You can produce {} in {} turns using robots {} with {}".format(robot, when,robots,produced_robot))
  return when

blueprint=blueprints[1]
storage=[0,0,0,0]
robots=[1,0,0,0]
robot_in_production=None
production_started=False
tLeft=24
goals=[Robots.geode]
for t in range (1,25):
  print("Minute {}".format(t))
  print("Storage: {}, Robots: {}".format(storage,robots))
  # if can produce robot.geode - produce robot geode
  tLeft=25-t
  geodes=0
  geodesP=0
  print("Production turns left:", tLeft)
  if can_produce(Robots.geode):
    start_production(Robots.geode)
  elif not robots[Robots.clay.value-1]:
    if verbose: print("There's no {}. Try to create one".format(Robots.clay))
    if can_produce(Robots.clay): start_production(Robots.clay)
  elif not robots[Robots.obsidian.value-1]:
    if verbose: print("There's no {}. Try to create one".format(Robots.obsidian))
    if can_produce(Robots.obsidian):
      start_production(Robots.obsidian)
  if not robot_in_production and can_produce(Robots.obsidian):
    geodes=simulate_production_ability(Robots.geode, None)
    geodesP=simulate_production_ability(Robots.geode, Robots.obsidian)
    print("bez prod {}, z prod {}".format(geodes, geodesP))
    if geodesP < geodes:
      start_production(Robots.obsidian)
  if not robot_in_production and can_produce(Robots.clay):
    without_clay=simulate_production_ability(Robots.obsidian, None)
    with_clay=simulate_production_ability(Robots.obsidian, Robots.clay)
    print("bez prod {}, z prod {}".format(without_clay, with_clay))
    if without_clay > with_clay:
      start_production(Robots.clay)
  collect()
  if robot_in_production: 
    finish_production()
  input()
print("Collected {} {}".format(storage[Mats.geode.value-1], Mats.geode))
print("storage:",storage)    
print("robots:", robots)

# run_scenario(initial_scenario, blueprints[1], t)
# for robot in blueprints[1][::-1]:
#   print(robot)
exit()

print("Start")
for bid, blueprint in enumerate(blueprints.values()):
  if verbose: print("Simulation for blueprint ", bid+1)
  for t in range(1,25):
    if verbose: print("Blueprint {}, {} minute".format(bid+1,t))  
    prod=[]
    print("TIme {}, scenarios {}".format(t,len(scenarios[t])))
    
    #for scenario in scenarios[t]:
    
    if verbose: print("Blueprint {}, minute {}, scenario {}".format(bid+1, t, scenario["id"]))
    if verbose: print("Mats:{}, robots:{}".format(scenario["storage"],scenario["robots"]))
    for idr,robot in enumerate(blueprint.keys()):
      if can_produce(blueprint[robot], scenario["storage"]):
        storage = list(scenario["storage"])
        robots = list(scenario["robots"])
        # New scenario! :)
        scid=scenario["id"]+"+"+str(idr)
        
        start_production(blueprint[robot], robot, storage)
        storage=collect(robots, storage)
        finish_production(robot, robots)
        if verbose: print("New scenario {}: producing {} {}".format(scid,robot,storage))
        new_scenario(t+1, scid, storage, robots)
        if verbose: input()
    if verbose: print("Starting NO ROBOTS scenario")
    storage=list(scenario["storage"])
    robots=list(scenario["robots"])
    scid=scenario["id"]+"+0"
    storage=collect(robots, storage)
    if verbose: print("New scenario {}: pass resources".format(scid))
    new_scenario(t+1, scid, storage, robots)
    if verbose: input()
print(scenarios[25])
exit()
# Blueprint 1:
#   Each ore robot costs 4 ore.
#   Each clay robot costs 2 ore.
#   Each obsidian robot costs 3 ore and 14 clay.
#   Each geode robot costs 2 ore and 7 obsidian.

# Blueprint 2:
#   Each ore robot costs 2 ore.
#   Each clay robot costs 3 ore.
#   Each obsidian robot costs 3 ore and 8 clay.
#   Each geode robot costs 3 ore and 12 obsidian.


print(Mats.ore)
for line in file:
  line=line.strip()
  print(line)
  text=line.split()
  for idl, text in enumerate(text):
    print(idl, text)

# 0 Blueprint
# 1 2:
# 2 Each
# 3 ore
# 4 robot
# 5 costs
# 6 2
# 7 ore.
# 8 Each
# 9 clay
# 10 robot
# 11 costs
# 12 3
# 13 ore.
# 14 Each
# 15 obsidian
# 16 robot
# 17 costs
# 18 3
# 19 ore
# 20 and
# 21 8
# 22 clay.
# 23 Each
# 24 geode
# 25 robot
# 26 costs
# 27 3
# 28 ore
# 29 and
# 30 12
# 31 obsidian.
file.close()
