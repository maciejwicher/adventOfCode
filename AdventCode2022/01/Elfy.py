file1 = open("c:/Users/nhmk36/Documents/Programming/Python/AdventCode2022/01/Elfy.txt", 'r')

emptyLines = 0
elfTotal=0
max1=0
max2=0
max3=0
while True:
    elfCalories = file1.readline().strip()
    print(elfCalories)
    


    if emptyLines == 1 and not elfCalories:
      print("Koniec. Trzy najwieksze kalorie to {}, {} i {}. Ich suma to: {}".format(max1, max2, max3, max1+max2+max3))
      break
    if not elfCalories:
        emptyLines=1
        if elfTotal>=max1:
          max3=max2
          max2=max1
          max1=elfTotal
        elif elfTotal>=max2:
          max3=max2
          max2=elfTotal
        elif elfTotal>=max3:
          max3=elfTotal


        elfTotal=0
    else:
        emptyLines=0
        elfTotal+=int(elfCalories)

    
  
file1.close()