#start
print("Welcome to the Tip Calculator")
#ask user for bill total
total_bill = input("What was your total bill?\n")
#ask user for tip percentage
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15?\n")
#ask user number to split by
num_to_split = input("How many people to split the bill?\n")

#Calculate Tip
total_tip = ((float(total_bill) / int(num_to_split)) * (int(tip_percentage)/100+1))
# (150.00 / 5) * 1.12 = 33.6
final_amount = round(total_tip, 2)

#Print Result
print(f"Each person should pay: {final_amount}")