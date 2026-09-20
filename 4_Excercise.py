# Two players simultaneously form one of three shapes: a fist (rock), a flat hand (paper), or a V (scissors). 
# Rock crushes scissors, scissors cuts paper, and paper covers rock.

import random 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

print("Let's Play Rock, Paper and Scissor")

choice = int(input(
    "What's your choice? 0 for Rock, 1 for Paper, 2 for Scissors: "
))

if choice < 0 or choice > 2:
    print("Wrong choice. Game Over!")

else:
    print("Your choice:")
    print(game_images[choice])

    comp_choice = random.randint(0, 2)

    print("Computer choice:")
    print(game_images[comp_choice])


    if choice ==  comp_choice :
        print("Game Draw")
    elif choice == 2 and comp_choice == 0:
        print("Comp Wins")
    elif choice == 0 and comp_choice == 2:
        print("You win!")
    elif choice > comp_choice:
        print("You Win")
    else:
            print("Comp Wins")