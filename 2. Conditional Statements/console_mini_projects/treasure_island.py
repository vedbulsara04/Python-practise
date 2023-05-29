# Treasure Island console project.

print('''
*******************************************************************************
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
''')

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

choice1 = input('You are at a crossroad, where do you want to go? Type "left" or "right" : ').lower()

if choice1 == "right":
    choice2 = input('''You have come to a lake..
There is an island in the middle of the lake. T
Type wait to "wait" to wait for a boat or "swim"
to swim accross the lake : ''').lower()

    if choice2 == "wait":
        choice3 = input('''You arrive at the island unharmed..
There is a house with 3 doors with colours Red, Yellow & Blue
Which colour do you choose ?''').lower()
       
        if choice3 == "Red":
            print("It is a room full of fire! Game Over.")
        elif choice3 == "Yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "Blue":
            print("You enter a room where LordTroldemort is waiting with his axe. Game Over!")
        else:
            print("The door does not exist!")
            
    else:
        print("You have been attacked by an angry trout! Game over.")
    
else:
    print("You fell in a trapdoor! Game over.")
