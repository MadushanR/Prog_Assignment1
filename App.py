'''This module receives user inputs, displays game rules and outputs respectively'''

import Shrek,Nemo,Game
shrek_attributes = Shrek.attributes() #This variable is to import shreks's attributes
nemo_attributes = Nemo.attributes()#This variable is to import nemo's attributes
print("\nWelcome to the games of shremo, you can choose 1 of 2 characters first as player 1 for this quest. \nEach character has 3 challenges which needs to be completed in order to win and each character has 3 different attributes\n")
print(f"Shrek has the below attributes\n1.Power : {shrek_attributes[2]}\n2.Intelligence : {shrek_attributes[1]}\n3.Jump : {shrek_attributes[0]}\n")
print(f"Nemo has the below attributes \n1.Swimming : {nemo_attributes[0]}\n2.Speed : {nemo_attributes[1]}\n3.Intelligence : {nemo_attributes[2]}\n")
character = int(input("Enter 1 to choose Shrek first or 2 to choose Nemo first\n")) #Gets the character choice of player 1
Shrek_Win_1 = False #This variable is to check if Shrek won the first challenge
Shrek_Win_2 = False #This variable is to check if Shrek won the second challenge
Shrek_Win_3 = False #This variable is to check if Shrek won the third challenge
Nemo_Win_1 = False #This variable is to check if Nemo won the first challenge
Nemo_Win_2 = False #This variable is to check if Nemo won the second challenge
Nemo_Win_3 = False #This variable is to check if Nemo won the third challenge
Shrek_Attribute_Avg = 0 #This variable for the average of attributes
Nemo_Attribute_Avg = 0 #This variable for the average of attributes

if character == 1 :
    print("Player 1 is Shrek and Player 2 is Nemo\n")
    input("As the first challenge you need to swim across a river full of crocodiles, you need a dice roll value above 5 to win\nPress enter to continue as Shrek")
    challenge_1 = Game.challenge_1(Shrek.jump) #This variable stores values returned by Game.challenge_1 function 
    dice_roll = challenge_1[0] #stores first value returned by  Game.challenge_1 function
    Shrek_Win_1 = challenge_1[1] #stores second value returned by  Game.challenge_1 function
    Shrek.jump =  challenge_1[2] #stores third value returned by  Game.challenge_1 function
    print(f"Your dice roll value is {dice_roll} and jump is {Shrek.jump}")
    if Shrek_Win_1 == True :
        input("You have won the first challenge \n\n For the second challenge you need to unlock the door ahead of you, you need a dice roll value above 7 to win \nPress enter to continue\n")
        challenge_2 = Game.challenge_2(Shrek.intelligence) #This variable stores values returned by Game.challenge_2 function 
        dice_roll = challenge_2[0] #stores first value returned by  Game.challenge_2 function
        Shrek_Win_2 = challenge_2[1] #stores second value returned by  Game.challenge_2 function
        Shrek.intelligence =  challenge_2[2] #stores third value returned by  Game.challenge_2 function
        print(f"Your dice roll value is {dice_roll} and intelligence is {Shrek.intelligence}")
        if Shrek_Win_2 == True :
            input("You have won the second challenge \n\n For the third and final challenge you need to fight the Mad King Arthur, you need a dice roll value above 9 to win\nPress enter to continue\n")
            challenge_3 = Game.challenge_3(Shrek.power) #This variable stores values returned by Game.challenge_2 function 
            dice_roll = challenge_3[0] #stores first value returned by  Game.challenge_2 function
            Shrek_Win_3 = challenge_3[1] #stores second value returned by  Game.challenge_2 function
            Shrek.power =  challenge_3[2] #stores third value returned by  Game.challenge_2 function
            print(f"Your dice roll value is {dice_roll} and power is {Shrek.power}")
            if Shrek_Win_3 == True :
                print("\nCongratulations you won the game\n")
            else :
                print("You lost the third round\n")
        else :
            print("You have lost the second round\n")
    else :
        print("You have lost the first round\n")
    
    print("\nWelcome Nemo\n")
    input("\nAs the first challenge you need to swim across a river full of crocodiles, you need a dice roll value above 5 to win\nPress enter to continue as Nemo")
    challenge_1 = Game.challenge_1(Nemo.swimmming)
    dice_roll = challenge_1[0]
    Nemo_Win_1 = challenge_1[1]
    Nemo.swimmming =  challenge_1[2]
    print(f"Your dice roll value is {dice_roll} and swimming is {Nemo.swimmming}")
    if Nemo_Win_1 == True :
        input("You have won the first challenge \n\n For the second challenge you need to unlock the door ahead of you, you need a dice roll value above 7 to win \nPress enter to continue\n")
        challenge_2 = Game.challenge_2(Nemo.intelligence)
        dice_roll = challenge_2[0]
        Nemo_Win_2 = challenge_2[1]
        Nemo.intelligence =  challenge_2[2]
        print(f"Your dice roll value is {dice_roll} and intelligence is {Nemo.intelligence}")
        if Nemo_Win_2 == True :
            input("You have won the second challenge \n\n For the third and final challenge you need to fight the Mad King Arthur, you need a dice roll value above 9 to win\nPress enter to continue\n")
            challenge_3 = Game.challenge_3(Nemo.speed)
            dice_roll = challenge_3[0]
            Nemo_Win_3 = challenge_3[1]
            Nemo.speed =  challenge_3[2]
            print(f"Your dice roll value is {dice_roll} and speed is {Nemo.speed}")
            if Nemo_Win_3 == True :
                print("\nCongratulations you won the game")
            else :
                print("You lost the third round\n")
        else :
            print("You have lost the second round\n")
    else :
        print("You have lost the first round\n")

else :

    print("Player 1 is Nemo and Player 2 is Shrek\n")
    input("As the first challenge you need to swim across a river full of crocodiles, you need a dice roll value above 5 to win\nPress enter to continue as Nemo")
    challenge_1 = Game.challenge_1(Nemo.swimmming)
    dice_roll = challenge_1[0]
    Nemo_Win_1 = challenge_1[1]
    Nemo.swimmming =  challenge_1[2]
    print(f"Your dice roll value is {dice_roll} and swimming is {Nemo.swimmming}")
    if Nemo_Win_1 == True :
        input("You have won the first challenge \n For the second challenge you need to unlock the door ahead of you, you need a dice roll value above 7 to win \nPress enter to continue\n")
        challenge_2 = Game.challenge_2(Nemo.intelligence)
        dice_roll = challenge_2[0]
        Nemo_Win_2 = challenge_2[1]
        Nemo.intelligence =  challenge_2[2]
        print(f"Your dice roll value is {dice_roll} and intelligence is {Nemo.intelligence}")
        if Nemo_Win_2 == True :
            input("You have won the second challenge \n For the third and final challenge you need to fight the Mad King Arthur, you need a dice roll value above 9 to win\nPress enter to continue\n")
            challenge_3 = Game.challenge_3(Nemo.speed)
            dice_roll = challenge_3[0]
            Nemo_Win_3 = challenge_3[1]
            Nemo.speed =  challenge_3[2]
            print(f"Your dice roll value is {dice_roll} and speed is {Nemo.speed}")
            if Nemo_Win_3 == True :
                print("Congratulations you won the game")
            else :
                print("You lost the third round")
        else :
            print("You have lost the second round")
    else :
        print("You have lost the first round")

    print("\nWelcome Shrek")
    input("As the first challenge you need to swim across a river full of crocodiles, you need a dice roll value above 5 to win\nPress enter to continue as Shrek")
    challenge_1 = Game.challenge_1(Shrek.jump)
    dice_roll = challenge_1[0]
    Shrek_Win_1 = challenge_1[1]
    Shrek.jump =  challenge_1[2]
    print(f"Your dice roll value is {dice_roll} and jump is {Shrek.jump}")
    if Shrek_Win_1 == True :
        input("You have won the first challenge \n For the second challenge you need to unlock the door ahead of you, you need a dice roll value above 7 to win \nPress enter to continue\n")
        challenge_2 = Game.challenge_2(Shrek.intelligence)
        dice_roll = challenge_2[0]
        Shrek_Win_2 = challenge_2[1]
        Shrek.intelligence =  challenge_2[2]
        print(f"Your dice roll value is {dice_roll} and intelligence is {Shrek.intelligence}")
        if Shrek_Win_2 == True :
            input("You have won the second challenge \n For the third and final challenge you need to fight the Mad King Arthur, you need a dice roll value above 9 to win\nPress enter to continue\n")
            challenge_3 = Game.challenge_3(Shrek.power)
            dice_roll = challenge_3[0]
            Shrek_Win_3 = challenge_3[1]
            Shrek.power =  challenge_3[2]
            print(f"Your dice roll value is {dice_roll} and power is {Shrek.power}")
            if Shrek_Win_3 == True :
                print("Congratulations you won the game")
            else :
                print("You lost the third round")
        else :
            print("You have lost the second round")
    else :
        print("You have lost the first round")


Shrek_Attribute_Avg = (Shrek.intelligence + Shrek.jump + Shrek.power)/3 #calculates average of attributes
Nemo_Attribute_Avg = (Nemo.intelligence + Nemo.speed + Nemo.swimmming)/3 #calculates average of attributes

if Shrek_Attribute_Avg > Nemo_Attribute_Avg : 
    print("\nShrek is the MVP") #if shrek's average is high then outputs shrek is MVP
elif Shrek_Attribute_Avg == Nemo_Attribute_Avg :
    print("\nNo MVP")
else :
    print("\nNemo is the MVP") #if nemo's average is high then outputs nemo is MVP
