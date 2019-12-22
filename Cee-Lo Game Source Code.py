#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Python Assignment
#Cee-Lo Dice Game

#Importing Random Library
import random

#Assigning variables to generate random numbers 
x = random.randint(1, 6)

y = random.randint(1, 6)

z = random.randint(1, 6)

sequence = [str(x),str(y),str(z)]

#Creating an empty list to store matches later on
match_lst = ["","",""]

point = 0

#Function to check dice matches
def check_dice_matches():
    count = 0
    for i in range(len(sequence)):
        if sequence[i] == match_lst[i]:
            count += 1

    print(str(count), 'Matches found')

#Function to check the winner (match found)
def checkWin(match_lst,sequence):
    if match_lst[0] == sequence[0] and match_lst[1] == sequence[1] and match_lst[2] == sequence[2]:

        print('-'.join(match_lst))
        return True
    else:
        return False

#Function to roll the dice (works on each roll)
def roll():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    print('Rolling Dice 1:', dice1)
    print('Rolling Dice 2:', dice2)
    print('Rolling Dice 3:', dice3)
    match_lst[0] = str(dice1)
    match_lst[1] = str(dice2)
    match_lst[2] = str(dice3)

    print('Your sequence','-'.join(match_lst))
    check_dice_matches()

#Main function defination
def ceelo_game():
    #For matching sequence
    point = 0
    total = 0
    print("Following is the sequence for the dice rolled:", '-'.join(sequence))
    roll()
    total += 3

    while True:

        if checkWin(match_lst,sequence) == True:
            print('your sequence matched')
            print('Total dices rolled',total)
            res =(point * (total/100))
            res2 = point - res
            print('Points taken',int(res2))
            break
            
        if match_lst[0] == sequence[0]:

            #20 points for each sucessfull match
            point += 20
            ask2 = input('which dice you want to roll?(1/2/3)')
            if ask2 == '1':
                dice1 = random.randint(1,6)
                print('Rolling dice 1:',dice1)
                total +=1
                match_lst[0] = str(dice1)
                print('Your sequence','-'.join(match_lst))
                check_dice_matches()

            elif ask2 == '2':
                dice2 = random.randint(1, 6)
                print('Rolling dice 2:', dice2)
                match_lst[1] = str(dice2)
                total += 1
                print('Your sequence', '-'.join(match_lst))
                check_dice_matches()

            elif ask2 == '3':
                dice3 = random.randint(1, 6)
                print('Rolling dice 3:', dice3)
                match_lst[2] = str(dice3)
                total += 1
                print('Your sequence', '-'.join(match_lst))
                check_dice_matches()

        elif match_lst[1] == sequence[1]:
            # 20 points for each sucessfull match
            point += 20
            ask2 = input('which dice you want to roll?(1/2/3)')
            if ask2 == '1':
                dice1 = random.randint(1,6)
                print('Rolling dice 1:',dice1)
                match_lst[0] = str(dice1)
                total += 1
                print('Your sequence','-'.join(match_lst))
                check_dice_matches()

            elif ask2 == '2':
                dice2 = random.randint(1, 6)
                print('Rolling dice 2:', dice2)
                match_lst[1] = str(dice2)
                total += 1
                print('Your sequence','-'.join(match_lst))
                check_dice_matches()

            elif ask2 == '3':
                dice3 = random.randint(1, 6)
                print('Rolling dice 3:', dice3)
                match_lst[2] = str(dice3)
                total += 1
                print('Your sequence','-'.join(match_lst))
                check_dice_matches()

        elif match_lst[2] == sequence[2]:
            # 20 points for each sucessfull match
            point += 20
            ask2 = input('which dice you want to roll?(1/2/3)')
            if ask2 == '1':
                dice1 = random.randint(1,6)
                print('Rolling dice 1:',dice1)
                match_lst[0] = str(dice1)
                total += 1
                print('Your sequence','-'.join(match_lst))
                check_dice_matches()

            elif ask2 == '2':
                dice2 = random.randint(1, 6)
                print('Rolling dice 2:', dice2)
                match_lst[1] = str(dice2)
                total += 1
                print('Your sequence', '-'.join(match_lst))
                check_dice_matches()

            elif ask2 == '3':
                dice3 = random.randint(1, 6)
                print('Rolling dice 3:', dice3)
                match_lst[2] = str(dice3)
                total += 1
                print('Your sequence', '-'.join(match_lst))
                check_dice_matches()
        else:
            ask = input('Sequence not matched. Want to reroll?(y/n)')
            if ask == 'y':
                roll()
                total += 3
            else:
                break

#Defining function to reroll the dice               
def reroll(match_lst):
    if match_lst[0] != sequence[0] and match_lst[1] != sequence[1] and match_lst[2] != sequence[2]:
        print('Sequence not been matched', '-'.join(match_lst))
        ask = input('Try again?(y/n)')
        if ask == 'y':
            roll()
        else:
            print('Bye')

ceelo_game()


# In[ ]:




