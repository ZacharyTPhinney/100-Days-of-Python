#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill = input("What was the bill amount?\n")
people = input("How many people were there?\n")
perc=  input("How much would you like to tip 10 12 or 15?\n")
intbill = float(bill)
intpeople = float(people)
intperc = float(perc)/100  +1
final = round((intbill/intpeople *intperc),2)
print(f"You should pay ${final}")
