from enum import Enum
import math
import sys



if len(sys.argv)>1:
  verbose=True
else:
  verbose = False
file=open('.\input-test.txt', 'r')

Mats = Enum('Mats', ['ore', 'clay', 'obsidian', 'geode'])
Robots = Enum('Robot', ['ore', 'clay', 'obsidian', 'geode'])



def collect(storage):
  
  storage=[x+y for x,y in zip(c_robots,storage)]
  #if verbose:
    #for i,r in enumerate(robots):
    #  if verbose: print("{} produced {} {}. You have {}".format(Robots(i+1), c_robots[i], Mats(i+1), storage[i]))
  return storage

def can_produce(robot):
  max_prod=10000
  global c_blueprint
  global c_storage
  robot_cost=c_blueprint[robot]
  if verbose: print("Determine if I can buy {} which cost {} with {}".format(robot, robot_cost,c_storage), end="")
  for idr, resource in enumerate(c_storage):
    if robot_cost[idr]:
      prod=c_storage[idr]//robot_cost[idr]
      max_prod=min(prod, max_prod)
  if max_prod:
    if verbose: print("...YES")
  else:
    if verbose: print("...NO")
  return max_prod

def start_production(robot, storage):
  global c_blueprint
  for idr, res in enumerate(c_blueprint[robot]):
    storage[idr]-=res
  #if verbose: print("Spend {} on {}. Left: {}".format(c_blueprint[robot], robot, storage))

def finish_production(robot,robots):
  robots[robot.value-1]+=1
  #if verbose: print("Finished production of {}. You have {}".format(robot,robots[robot.value-1]))

def when_produce(cost, robot, storage):
  #cost=blueprint[robot]
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
blueprints = { 1: { Robots(1): [4,0,0,0], Robots(2): [2,0,0,0], Robots(3): [3,14,0,0], Robots(4): [2,0,7,0]}}


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

robot_states={}
blueprint=blueprints[1]
storage=[0,0,0,0]
robots=[1,0,0,0]
robot_in_production=None
production_started=False
tLeft=24
def new_scenario(t, sid, storage, robots):
  scenarios[t]=scenarios.get(t,[])
  scenarios[t].append({"id": sid, "storage": storage, "robots": robots})
  if verbose: print("created new scenario:", scenarios[t][-1])
scenarios={ x: [] for x in range(1,25) }
new_scenario(1, "", [0,0,0,0], [1,0,0,0] )

c_blueprint=None
c_storage=None
c_robots=None
scenario_ids=[]
limit={Robots.ore: 4, Robots.clay:10, Robots.obsidian: 16, Robots.geode: 50 }
print("Start")
for bid, blueprint in enumerate(blueprints.values()):
  if verbose: print("Simulation for blueprint ", bid+1, " *****************")
  c_blueprint=blueprint
  for t in range(1,25):
    if verbose: print("Blueprint {}, {} minute".format(bid+1,t))  
    prod=[]
    print("Time {}, scenarios {}".format(t,len(scenarios[t])), "**************")
    if verbose:
      for sc in scenarios[t]:
        print(sc["id"])    
    for ids, scenario in enumerate(scenarios[t]):
      c_storage=scenario["storage"]
      c_robots=scenario["robots"]

      if verbose: print("Scenario {} ({} of {})".format(scenario["id"], ids+1, len(scenarios[t])))
      if verbose: print("Mats:{}, robots:{}".format(c_storage,c_robots))
      produced = {}
    
      for idr,robot in enumerate(c_blueprint.keys()):
        if verbose: print("Exam robot {}".format(robot))
        if can_produce(robot) and limit[robot]>c_robots[robot.value-1]:
          if can_produce(Robots.geode) and robot.value != Robots.geode.value:
            continue
          elif can_produce(Robots.obsidian) and robot.value != Robots.obsidian.value:
            continue
          #print("")
          if verbose: print("Starting CREATE ", robot, " scenario ")
          storage = list(c_storage)
          robots = list(c_robots)
          # New scenario! :)
          scid=scenario["id"]+str(idr+1)
          if verbose: print("Creating scenario {}".format(scid))
          
          start_production(robot, storage)
          storage=collect(storage)
          finish_production(robot, robots)
          if int(scid) not in scenario_ids:
            scenario_ids.append(int(scid))
            if verbose: print("New scenario {}: producing {} {}".format(scid,robot,storage))
            new_scenario(t+1, scid, storage, robots)
          else:
            pass
            if verbose: print("Scenario {} already in scenarios ({})".format(scid, scenario_ids))
          
      ##print("")
      # if verbose: print("Starting NO ROBOTS scenario")
      # if (scenario["robots"][Robots.clay.value-1] > 0) and \
      #    (scenario["robots"][Robots.obsidian.value-1] == 0 or scenario["robots"][Robots.geode.value-1] == 0):
      #   continue
      storage=list(scenario["storage"])
      robots=list(scenario["robots"])
      scid=scenario["id"]+"0"
      storage=collect(storage)
      #if verbose: print("New scenario {}: pass resources".format(scid))
      new_scenario(t+1, scid, storage, robots)
      if verbose: input()
max_geode=0
for sc in scenarios[25]:
  if (sc["storage"])[3] > max_geode:
    max_geode=(sc["storage"])[3]
print("Max geodes:", max_geode)
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


file.close()
