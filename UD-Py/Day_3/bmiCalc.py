#Request user input
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#Use input to calculate users BMI
BMI = int(weight) / float(height) ** 2

#convert BMI to int (rounds )
bmi_as_int = int(BMI)

#Print result 
print (bmi_as_int)


