from enum import Enum
import math
import sys
import re

# 16926 that's the answer for the current data set, scenario 2

# For simple debug
verbose = True if len(sys.argv)>1 else False

Mats = Enum('Mats', ['ore', 'clay', 'obsidian', 'geode'])
Robots = Enum('Robot', ['ore', 'clay', 'obsidian', 'geode'])

blueprints = { }


def collect(production, storage):
  storage=[x+y for x,y in zip(production,storage)]
  if verbose:
    for i,r in enumerate(robots):
      print("{} produced {} {}. You have {}".format(Robots(i+1), c_robots[i], Mats(i+1), storage[i]))
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
  if verbose: print("Spend {} on {}. Left: {}".format(c_blueprint[robot], robot, storage))

def finish_production(robot,robots):
  robots[robot.value-1]+=1
  if verbose: print("Finished production of {}. You have {}".format(robot,robots[robot.value-1]))

def read_blueprints():
  global blueprints
  bps = open('.\input.txt', 'r')
  while True:
    bp=bps.readline().strip()
    if not bp:
      break
    if verbose: print("read line: ", bp)
    cmdResult = re.search(r'Blueprint (\d+): .*ore robot.* (\d+).*clay robot.* (\d+).*obsidian.* (\d+) ore.* (\d+).*geode.* (\d+).* (\d+).*', bp)
    if cmdResult:
      bpNr, cOre, cClay, cObs1, cObs2, cGeo1, cGeo2 = cmdResult.groups()
      blueprints[int(bpNr)]={ 
        Robots(1): [int(cOre), 0, 0, 0], 
        Robots(2): [int(cClay), 0, 0, 0], 
        Robots(3): [int(cObs1), int(cObs2), 0, 0], 
        Robots(4): [int(cGeo1), 0, int(cGeo2), 0]}

def new_scenario(t, sid, storage, robots, doNotProduce={}):
  scenarios[t]=scenarios.get(t,[])
  scenarios[t].append({"id": sid, "storage": storage, "robots": robots, "doNotProduce": doNotProduce})
  if verbose: print("created new scenario:", scenarios[t][-1])

read_blueprints()

blueprint=blueprints[1]
storage=[0,0,0,0]
robots=[1,0,0,0]

c_blueprint=None
c_storage=None
c_robots=None
geode_produced=False
exclude_not_geode=False
limit={Robots.ore: 4, Robots.clay:10, Robots.obsidian: 16, Robots.geode: 50 }
print("Start")
result=1
for blueprint_id in range(1,4):
  scenarios={ x: [] for x in range(1,33) }
  new_scenario(1, "", [0,0,0,0], [1,0,0,0] )
  geode_produced=False
  exclude_not_geode=False
  if verbose: print("Simulation for blueprint ", blueprint_id, " *****************")
  c_blueprint=blueprints[blueprint_id]
  for t in range(1,33):
    if verbose: print("Blueprint {}, {} minute".format(blueprint_id,t))  
    prod=[]
    print("Time {}, scenarios {}".format(t,len(scenarios[t])))
    if geode_produced: 
      exclude_not_geode=True 
    for ids, scenario in enumerate(scenarios[t]):
      c_storage=scenario["storage"]
      c_robots=scenario["robots"]
      c_doNotProduce=scenario["doNotProduce"]
      if verbose: print("Scenario {} ({} of {})".format(scenario["id"], ids+1, len(scenarios[t])))
      if verbose: print("Mats:{}, robots:{}".format(c_storage,c_robots))
      produced = {}
      doNotProduce={}
      if exclude_not_geode and str(geode_produced) not in scenario["id"]: 
        continue
      for robot in c_blueprint.keys():
        if can_produce(robot):
          doNotProduce[robot.value]=1
      for idr,robot in enumerate(c_blueprint.keys()):
        
        if c_doNotProduce.get(idr+1, None):
          if verbose: print("Cannot produce robot {}".format(robot))
          continue
        if verbose: print("Exam robot {}".format(robot))
        if can_produce(robot): 
          if limit[robot]<=c_robots[robot.value-1]: continue
          if can_produce(Robots.geode) and robot.value != Robots.geode.value: continue
          if verbose: print("Starting CREATE ", robot, " scenario ")
          storage = list(c_storage)
          robots = list(c_robots)
          # New scenario! :)
          scid=scenario["id"]+str(idr+1)
          if verbose: print("Creating scenario {}".format(scid))
          
          start_production(robot, storage)
          storage=collect(robots, storage)
          finish_production(robot, robots)
          new_scenario(t+1, scid, storage, robots, {})
          if robot==Robots.geode: 
            geode_produced=Robots.geode.value

      storage=list(scenario["storage"])
      robots=list(scenario["robots"])
      scid=scenario["id"]+"0"
      storage=collect(robots, storage)
      new_scenario(t+1, scid, storage, robots, doNotProduce)
      if verbose: input()
  
  max_geode=0
  for sc in scenarios[33]:
    if (sc["storage"])[3] > max_geode:
      max_geode=(sc["storage"])[3]
  result*=max_geode
  print("BP: {} Max geodes:{}, multi: {}".format(blueprint_idl,max_geode, result))
exit()
