#Kaun banega crorepathi Game
a=input("What's your name? ")
print("Welcome to the 1st Season of Kaun Banega Crorepathi!",a)

print('''GameRules:\n You have 3 Levels in this game\n1.The first level ends when you complete the 2nd Question,even if the 3rd Question is wrong you will retain the amount that you won till 2nd question.\n
2.The Second level ends when you complete the 4th Question,even if the 5th Question is wrong you will retain the amount that you won till 4th question.\n
3.If you answer the 5th Question correctly you will win a jackpot price of 160000 and a BenzCar worth 4500000.\n
4.If you are not sure of the answer you  can quit at any point of time.\n
ALL THE BEST!!''')

Questions=[["Grand Central Terminal, Park Avenue, New York is the world's","largest railway station","highest railway station","longest railway station","None of the above",1],

["Entomology is the science that studies","Behavior of human beings","Insects","The origin and history of technical and scientific terms","The formation of rocks",2],

["For which of the following disciplines is Nobel Prize awarded?","Physics and Chemistry","Physiology or Medicine","Literature, Peace and Economics","All of the above",4],

["ICAO stands for","International Civil Aviation Organization","Indian Corporation of Agriculture Organization","Institute of Company of Accounts Organization",
"None of the above",1],

["India has largest deposits of ____ in the world","gold","copper","mica","None of the above",3]]

PriceMoney=[10000,20000,40000,80000,160000]
money=0
for i in range(0,len(Questions)):
    Question=Questions[i]
    print(f"\n\nQuestion for Rs. {PriceMoney[i]}")
    print(f"{Question[0]}")
    print(f"a. {Question[1]}          b. {Question[2]} ")
    print(f"c. {Question[3]}          d. {Question[4]} ")
    Response = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
    if (Response == 0):
     money = PriceMoney[i-1]
     break
    if(Response == Question[-1]):
     print(f"Wohoo!! Correct answer, you have won Rs. {PriceMoney[i]}")
     if(i == 1):
      money = 20000
     elif(i == 3):
      money = 80000
     elif(i == 4):
      money = 160000
    else:
     print("Oops!! Wrong answer")
     break 

print(f"Your take home money is {money}")
