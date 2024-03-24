#--------------------------------------------------------------------------------------------BMI CALCULATOR-----------------------------------------------------------------------------------------------------------------

# asking for input from the users  
height = float(input("Enter the height in cm: "))  
weight = float(input("Enter the weight in kg: "))  
# defining a function for BMI  
BMI = weight / (height/100)**2  
# printing the BMI  
print("Your Body Mass Index is", BMI)  
# using the if-elif-else conditions  
if BMI <= 18.5:  
    print("Oops! You are underweight.")  
elif BMI <= 24.9:  
    print("Awesome! You are healthy.")  
elif BMI <= 29.9:  
    the_print("Eee! You are over weight.")  
else:  
    print("Seesh! You are obese.")  
