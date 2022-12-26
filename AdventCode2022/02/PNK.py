file1 = open("c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/02/PNK.txt", 'r')

# X Y Z rock, papers, scisors przegrana remis wygrana
# A B C rock, papers, scisors
# A=1
# B=2
# C=3

info={  "who_beats_me":{ "rock": "paper", "paper": "scisors", "scisors": "rock" },
        "who_i_beat":{"rock": "scisors", "scisors": "paper", "paper": "rock" },
        "who_i_draw": {"rock": "rock", "scisors": "scisors", "paper": "paper" }
 
}

translate_function={"X": "who_i_beat", "Y": "who_i_draw", "Z": "who_beats_me" }

score = { "shape": { "rock": 1, "paper": 2, "scisors": 3 },
           "game": { "X": 0, "Y": 3, "Z": 6 } }
translate_shape = { "A": "rock", "B": "paper", "C": "scisors" }

results = { "scisors"}
def co_zagrac(onGra, wynik):
    moj_wybor=None



strategy = { 
           "A X": 4,
           "A Y": 8,
           "A Z": 3,
           "B X": 1,
           "B Y": 5,
           "B Z": 9,
           "C X": 7,
           "C Y": 2,
           "C Z": 6
           }

total=0
roundNumber=0
while True:
    roundNumber+=1
    runda = file1.readline().strip()
    if not runda:
      break

    opponentShape, result=runda.split()
    print("Runda {}. Przeciwnik gra {} a ja musze {}".format(roundNumber,opponentShape,result))
    oponentShapeName=translate_shape[opponentShape]
    evalFunction=translate_function[result]
    print("Przeciwnik zagral {}, ja szukam {}".format(oponentShapeName,evalFunction))
    myShape=info[evalFunction][oponentShapeName]
    myScore=score["shape"][myShape]
    gameTotal=myScore+score["game"][result]
    print("Powinienem zagrac {}. dostane za niego {}, a za cala gre {}".format(myShape,myScore, gameTotal))

    total+=gameTotal
         
file1.close()
print("Twoj wynik to: {}".format(total))