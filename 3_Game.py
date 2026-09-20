print('''
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island. Your mission is to find the treasure")
direction = input("Where do you want to go left or right? ").lower()
if direction == "left":
    cross = input("How do you want to cross the lake: swim or wait? ").lower()
    if cross == "wait":
        door = input("Which door you want to knock: Red, Blue, Yellow? ").lower()
        if door == "blue":
            print("Eaten by beasts.Game Over.")
        elif door == "red":
            print("Burned by fire. Game Over.")
        elif door == "yellow":
            print("You won the game!")
        else:
            print("Game Over!")
    else:
        print("Attacked by trout.Game Over.")
else:
    print("Fall into a hole.Game Over.")





#Another if and else
# # Below 10 → "Cold"
# # 10–24 → "Nice"
# # 25–34 → "Warm"
# # 35+ → "Hot"

# temp = float(input("Enter the temperature: "))

# if temp < 10:
#     print("Cold")
# elif temp <= 24:
#     print("Nice")
# elif temp <= 34:
#     print("Warm")
# else:
#     print("Hot")



