#ask user to provide their age
age = input("What is your current age?\n")
myAge = int(age)

#Use input to calculate how long until user reachs age of 90
days_left = 32850 - (myAge * 365)
weeks_left =  4680 - (myAge * 52)
months_left = 1080 - (myAge * 12)

#Use f string to print result of calculation
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left")

"""
--Notes--
365 days = 1 year
52 weeks = 1 year
12 months = 1 year

32,850 days = 90 years  
4,680 weeks = 90 years  
1080 months = 90 years  

days_lived = (myAge * 365)
weeks_lived = (myAge * 52)
months_lived = (myAge * 12)

total_days_90_years = (32850)
total_weeks_90_years = (4680)
total_months_90_years = (1080)
"""