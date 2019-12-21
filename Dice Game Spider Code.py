#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Assignment 
#Spider Game 

#Importing random library 
import random

#Creating variables for each player
playerx1 = ["","","","","","","","","",""]
playerx2 = ["","","","","","","","","",""]
playerx3 = ["","","","","","","","","",""]
playerx4 = ["","","","","","","","","",""]

#Greeting the user
print("Welcome to the game! ")
print("How many players do u want? (2-4)")
player = int(input())

#Display function 
def display(lst):
    for char in lst:
        if char in "//\(OO)/\\":
            print(char, end = ' ')
            
#Creating main function for the spider game
def spider(player1, player2, player3, player4):

    #Describing the rules to the user
    print("Each player will be given a chance to throw a dice and whoever complete the spider first will win! ")
    
    i = 0
    k = 0
    j = 0
    l = 0
    
    #A loop for providing the condition
    while (True):
        
        x = random.randint(1,6)
        y = random.randint(1,6)
        a = random.randint(1,6)
        b = random.randint(1,6)
        
        #Parameters for creating the spider 
        #For First Player
        #For spider's body
        if (x==6):

            if (player1[3] != "("):
                player1[3] = "("
            else:
                player1[6] = ")"
                
        #For spider's eyes        
        if (x == 1):
            if player1[3] == "(" and player1[6] == ")":
                if (player1[4] != "O"):
                    player1[4] = "O"
                else:
                    player1[5] = "O"
                
        #For spider's legs
        if (x == 4 or x == 3):
            if player1[3] == "(" and player1[6] == ")":
            
                if (player1[0] != "/"):
                    player1[0] = "/"
                elif (player1[1] != "/"):
                    player1[1] = "/"
                elif (player1[2] != "\\"):
                    player1[2] = "\\"
                elif (player1[7] != "/"):
                    player1[7] = "/"
                elif (player1[8] != "\\"):
                    player1[8] = "\\"
                elif (player1[9] != "\\"):
                    player1[9] = "\\"
        
        #For increment
        i += 1
        
        #Printing out the status of first player
        ch = ''
        ch = ch.join(playerx1)
        print('Player 01 Status:',ch)
  
        if (player1[0] == "/" and player1[1] == "/" and player1[2] == "\\" and
            player1[3] == "(" and player1[4] == "O" and player1[5] == "O" and
            player1[6] == ")" and player1[7] == "/" and player1[8] == "\\" and
            player1[9] == "\\"):
            
            #First player winning message
            print("Player 01 won in "+str(i)+" tries! ")
            print(r"//\(OO)/\\")
            break
        
        #For Second Player
        if (y == 6):
            if (player2[3] != "("):
                player2[3] = "("
            else:
                player2[6] = ")"
                
        if (y == 1):
            if player2[3] == "(" and player2[6] == ")":
                if (player2[4] != "O"):
                    player2[4] = "O"
                else:
                    player2[5] = "O"
                
        if (y == 4 or y == 3):
            if player2[3] == "(" and player2[6] == ")":
                if (player2[0] != "/"):
                    player2[0] = "/"
                elif (player2[1] != "/"):
                    player2[1] = "/"
                elif (player2[2] != "\\"):
                    player2[2] = "\\"
                elif (player2[7] != "/"):
                    player2[7] = "/"
                elif (player2[8] != "\\"):
                    player2[8] = "\\"
                elif (player2[9] != "\\"):
                    player2[9] = "\\"
                
        #Status for second player
        ch1 = ''
        ch1 = ch1.join(player2)
        print("Player 02 Status: ",ch1)

        
        k += 1
        if (player2[0] == "/" and player2[1] == "/" and player2[2] == "\\" and
            player2[3] == "(" and player2[4] == "O" and player2[5] == "O" and
            player2[6] == ")" and player2[7] == "/" and player2[8] == "\\" and
            player2[9] == "\\"):
            
            #Second player winning message
            print("Player 02 won in ",k," tries! ")
            print(r"//\(OO)/\\")
            break

        #For Third Player
        if (a == 6):
            if (player3[3] != "("):
                player3[3] = "("
            else:
                player3[6] = ")"
                
        if (a == 1):
            if player3[3] == "(" and player3[6] == ")":
                if (player3[4] != "O"):
                    player3[4] = "O"
                else:
                    player3[5] = "O"
                
        if (a == 4 or a == 3):
            if player3[3] == "(" and player3[6] == ")":
                if (player3[0] != "/"):
                    player3[0] = "/"
                elif (player3[1] != "/"):
                    player3[1] = "/"
                elif (player3[2] != "\\"):
                    player3[2] = "\\"
                elif (player3[7] != "/"):
                    player3[7] = "/"
                elif (player3[8] != "\\"):
                    player3[8] = "\\"
                elif (player3[9] != "\\"):
                    player3[9] = "\\"

        if (player == 3 or player == 4):
            ch2 = ''
            ch2 = ch2.join(player3)
            print("Player 03 Status: " ,ch2)
            
            #Variable for increment
            j += 1
            if (player3[0] == "/" and player3[1] == "/" and player3[2] == "\\" and
                player3[3] == "(" and player3[4] == "O" and player3[5] == "O" and
                player3[6] == ")" and player3[7] == "/" and player3[8] == "\\" and
                player3[9] == "\\"):
                
                #Third player's winning message 
                print("Player 03 won in ",j," tries! ")
                print(r"//\(OO)/\\")
                break
        
        #For Forth Player 
        if (b == 6):
            if (player4[3] != "("):
                player4[3] = "("
            else:
                player4[6] = ")"
                
        if(b == 1):
            if player4[3] == "(" and player4[6] == ")":
                if (player4[4] != "O"):
                    player4[4] = "O"
                else:
                    player4[5] = "O"
                
        if (b == 4 or b == 3):
            if player4[3] == "(" and player4[6] == ")":
                if (player4[0] != "/"):
                    player4[0] = "/"
                elif (player4[1] != "/"):
                    player4[1] = "/"
                elif (player4[2] != "\\"):
                    player4[2] = "\\"
                elif (player4[7] != "/"):
                    player4[7] = "/"
                elif (player4[8] != "\\"):
                    player4[8] = "\\"
                elif (player4[9] != "\\"):
                    player4[9] = "\\"

        if (player == 4):
            #printing out fourth player's status
            ch3 = ''
            ch3 = ch3.join(player4)
            print("Player 04 status: " ,ch3)
            
            l += 1
            if (player4[0] == "/" and player4[1] == "/" and player4[2] == "\\" and
                player4[3] == "(" and player4[4] == "O" and player4[5] == "O" and
                player4[6] == ")" and player4[7] == "/" and player4[8] == "\\" and
                player4[9] == "\\"):
                
                #Printing fourth player's winning message
                print("Player 04 won in ",l," tries! ")
                print(r"//\(OO)/\\")
                break
                
#Calling spider() function
spider(playerx1, playerx2, playerx3, playerx4)

#Loop for asking the user to restart the game 
while(True):
    print("Do you want to play again? (y,n)")
    i = input()
    
    #If the user wants to play again
    if (i == "y"):
        player = int(input('How many players are there? '))
        playerx1 = ["","","","","","","","","",""]
        playerx2 = ["","","","","","","","","",""]
        playerx3 = ["","","","","","","","","",""]
        playerx4 = ["","","","","","","","","",""]
        spider(playerx1,playerx2,playerx3,playerx4)
    else:
        print("Bye!")
        break         


# In[ ]:




