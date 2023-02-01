'''This module receives user inputs, displays game rules and outputs respectively'''

import Shrek,Nemo
shrek_attributes = Shrek.attributes() 
nemo_attributes = Nemo.attributes()#This variable is to import nemo's attributes
print("Welcome to the games of shremo, you can choose 1 of 2 characters for this quest. \nEach character has 3 challenges which needs to be completed in order to win and each character has 3 different attributes\n")
print(f"Shrek has the below attributes\n1.Power : {shrek_attributes[3]} 2.Intelligence : {shrek_attributes[1]} 3.Swimming : {shrek_attributes[0]}\n")
print(f"Nemo has the below attributes \n1.Language : {nemo_attributes[0]}\n2.Speed : {nemo_attributes[1]}\n3.Jump : {nemo_attributes[2]}\n")
character = input("Enter 1 to choose Shrek first or 2 to choose Nemo first")