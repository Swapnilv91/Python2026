# # PEDMASLR - Rule of excuting mathematical expression 
# print(1 + 1)
# print(6 +  1)
# print(10 * 2)
# print(10 / 2) #float
# print(10 // 2) #int
# print(2 ** 2)

# # fun converts from other data type to required data types
# #int, str , float , bool are the functions.

# #with f string we can mixed up different datatypes with print function 

# score = 1
# height = 120
# winning = True

# print(f"Your score is : {score}. Your height is: {height}. And You are winning the game : {winning}")

#Tip Calcualtor
print("Welcome to the Tip Calcualtor!")

total_bill= int(input("What was the total bill: $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15: "))
split = int(input("How many ppl will splitt the bill: "))
final_bill = total_bill + (total_bill * (tip/100)) 
share = round((final_bill / split),2)
print (f"Each person should pay: {share}")