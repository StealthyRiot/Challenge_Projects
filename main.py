#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")
#Solution shows you could have done it like: bill = float(input("What was the total bill? $"))
bill = input("what was the total bill? $")
tip_percent = input("what percent tip would you like to give? 10, 12, or 15? ")
split = input("How many people to split the bill? ")

tip = float(tip_percent)
tipmult = 1 + float(tip / 100)

total_bill = float(float(bill) * float(tipmult))
amount = float(total_bill / float(split))
amount = "{:.2f}".format(amount)
print(f"Each person should pay: ${amount}")