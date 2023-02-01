'''This module receives user inputs, displays game rules and outputs respectively'''

import Shrek,Nemo,Game
shrek_attributes = Shrek.attributes() 
nemo_attributes = Nemo.attributes()#This variable is to import nemo's attributes
print("\nWelcome to the games of shremo, you can choose 1 of 2 characters first as player 1 for this quest. \nEach character has 3 challenges which needs to be completed in order to win and each character has 3 different attributes\n")
print(f"Shrek has the below attributes\n1.Power : {shrek_attributes[2]}\n2.Intelligence : {shrek_attributes[1]}\n3.Jump : {shrek_attributes[0]}\n")
print(f"Nemo has the below attributes \n1.Swimming : {nemo_attributes[0]}\n2.Speed : {nemo_attributes[1]}\n3.Intelligence : {nemo_attributes[2]}\n")
character = int(input("Enter 1 to choose Shrek first or 2 to choose Nemo first\n"))
Shrek_Win_1 = False
Shrek_Win_2 = False
Shrek_Win_3 = False
Nemo_Win_1 = False
Nemo_Win_2 = False
Nemo_Win_3 = False
Shrek_Attribute_Avg = 0
Nemo_Attribute_Avg = 0

if character == 1 :
    print("Player 1 is Shrek and Player 2 is Nemo\n")
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

