'''this module has the common functions needed for both roles'''
import random
win = False

def challenge_1(attribute):#this function calculates random number between 1 - 12 for diceroll and determines attribute values as per dice roll
    global win
    dice_roll = random.randrange(1,13)#stores a random value between 1 - 12
    if dice_roll>5: #if dice roll is above 5 then user wins
        win = True
    else : #if dice roll is less than 5 then user loses
        win = False
    if dice_roll<4:#reduces attribute level if dice roll is too low
        attribute-=1
    elif dice_roll>10:#increases attribute level if dice roll is too high
        attribute+=1
    return dice_roll,win,attribute #returns dice roll value, attribute value and win status

def challenge_2(attribute):#this function calculates random number between 1 - 12 for diceroll and determines attribute values as per dice roll
    global win
    dice_roll = random.randrange(1,13)#stores a random value between 1 - 12
    if dice_roll>7:
        win = True
    else :
        win = False
    if dice_roll<4:#reduces attribute level if dice roll is too low
        attribute-=1
    elif dice_roll>10:#increases attribute level if dice roll is too high
        attribute+=1
    return dice_roll,win,attribute

def challenge_3(attribute):#this function calculates random number between 1 - 12 for diceroll and determines attribute values as per dice roll
    global win
    dice_roll = random.randrange(1,13)#stores a random value between 1 - 12
    if dice_roll>9  :
        win = True
    else :
        win = False
    if dice_roll<4:#reduces attribute level if dice roll is too low
        attribute-=1
    elif dice_roll>5:#increases attribute level if dice roll is too high
        attribute+=1
    return dice_roll,win,attribute