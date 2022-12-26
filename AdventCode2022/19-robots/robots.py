from enum import Enum

file=open('.\input-test.txt', 'r')
Mats = Enum('Mats', ['ore', 'clay', 'obsidian', 'geode'])
Robots = Enum('Robot', ['ore', 'clay', 'obsidian', 'geode'])

verbose = False
def collect(robots, storage):
  collected=list[robots]
  storage=[x+y for x,y in zip(robots,storage)]
  if verbose:
    for i,r in enumerate(robots):
      if verbose: print("{} produced {} {}. You have {}".format(Robots(i+1), robots[i], Mats(i+1), storage[i]))
  return storage

def can_produce(cost,storage):
  max_prod=10000
  
  if verbose: print("Determine if I can buy {} with {}".format(cost,storage), end="")
  for idr, resource in enumerate(storage):
    if cost[idr]:
      prod=storage[idr]//cost[idr]
      max_prod=min(prod, max_prod)
  if max_prod:
    if verbose: print("...YES")
  else:
    if verbose: print("...NO")
  return max_prod

def start_production(blueprint, robot, storage):
  if verbose: print("Spend {} on {}".format(blueprint, robot))
  for idr, res in enumerate(blueprint):
    storage[idr]-=res

def finish_production(robot, robots):
  robots[robot.value-1]+=1
  
  if verbose: print("Finished production of {}. You have {}".format(robot,robots[robot.value-1]))

def new_scenario(t, sid, storage, robots):
  scenarios[t]=scenarios.get(t,[])
  scenarios[t].append({"id": sid, "storage": storage, "robots": robots})
  if verbose: print("created new scenario:", scenarios[t][-1])

def run_scenario(scenario):

  pass

blueprints = { 1: { Robots(1): [4,0,0,0], Robots(2): [2,0,0,0], Robots(3): [3,14,0,0], Robots(4): [2,0,7,0]}}
if verbose: print(blueprints)
if verbose: print(blueprints[1][Robots.ore])
# scenarios for each minute
scenarios={ x: [] for x in range(1,25) }
new_scenario(1, "1", [0,0,0,0], [1,0,0,0] )

run_scenario(scenarios[1])

t=1 
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
