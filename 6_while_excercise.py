# 
# The user gets 5 attempts to guess it.

# secret_number = 7
# attempt = 0 
# game = False
# while not game and attempt < 5:
#             number = int(input("Enter your number: "))
#             if secret_number == number:
#                 print("Your guess correct!")
#                 game = True
#             elif number > secret_number:
#                 print ("Too high")
#             else:
#                 print("Too low")
#             attempt = attempt + 1 

# if attempt == 5 and game == False:
#  print("You Lost")


# ATM 

# Option 1 — Check Balance: Print the current balance.
# Option 2 — Deposit: Ask how much to deposit, then add it to balance.
# Option 3 — Withdraw: Ask how much to withdraw. If the amount is greater than the balance, print "Insufficient balance". Otherwise, subtract it.
# Option 4 — Exit: Print "Thank you!" and stop the while loop.
# Anything else: print "Invalid option" and show the menu again.

print("Welcome to Python ATM")

menu = """
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
"""

balance = 1000

print(menu)
menu_choice = int(input("Choose an option: "))

while menu_choice != 4:

    if menu_choice == 1:
        print(f"Current balance: ${balance}")

    elif menu_choice == 2:
        deposit_amount = int(input("How much would you like to deposit? $"))

        balance += deposit_amount
        print(f"Current balance: ${balance}")

    elif menu_choice == 3:
        withdraw_amount = int(input("How much would you like to withdraw? $"))

        if withdraw_amount >= balance:
            print("Insufficient balance.")
        else:
            balance -= withdraw_amount
            print(f"Current balance: ${balance}")

    else:
        print("Invalid option.")

    print(menu)
    menu_choice = int(input("Choose an option: "))

print("Thanks for using Python ATM!")



