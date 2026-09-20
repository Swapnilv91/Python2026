import random 

# ran_int = random.randint(0,1) #return random nummber between 0,1
# if ran_int == 0:
#     print("HEAD")
# else:
#     print ("TAIL")

#List
#Ordered data type 
# canadian_provinces = [
#     "Alberta",
#     "British Columbia",
#     "Manitoba",
#     "New Brunswick",
#     "Newfoundland and Labrador",
#     "Nova Scotia",
#     "Ontario",
#     "Prince Edward Island",
#     "Quebec",
#     "Saskatchewan"
# ]
# print(canadian_provinces[0])
# print(canadian_provinces[-1])
# canadian_provinces.append("Swpnil")
# print(canadian_provinces)


#Select Random name from list

User= ["SV", "SH","VR","PG","HJ"]
length = len(User) - 1
choice = random.randint(0,length)
print(User[choice])