#Oasis Infobyte Python Programming Internship 
#PROJECT: BMI CALCULATOR(TASK - 1)
#Author: Jajala Srivalli

def calculate_bmi(weight,height):
    bmi=((weight)/(height**2))
    bmi=round(bmi,2)

    if(bmi<18.5):
        category="Underweight"
    elif(bmi<25):
        category="Normal"
    elif(bmi<30):
        category="Overweight"
    else:
        category="Obesity"

    return bmi,category

def bmi_print():
    print("BMI CALCULATOR")
     
    try:
        weight=float(input("Enter your weight in kgs: "))
        height=float(input("Enter your height in meters: " ))

        if(weight<=0 or height <=0 or height>3.0):
            print("Invalid Input Values. ")
        else:
             bmi,category=calculate_bmi(weight,height)
             print("BMI = ",bmi)
             print("Category = ",category)
    except ValueError:
        print("Enter only Numbers..")

bmi_print()