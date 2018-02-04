import time

height = int(input("Please enter your height in inchs: "))
print (" ")           
weight = int(input("Please enter your weight in pounds: "))
print (" ")           
bmi = weight * 703 / pow(height,2)

if bmi < 18.5:
    print("BMI: {0:.2f}".format(bmi)) 
    print("person is underweight")
elif bmi >= 18.5 and bmi < 25:
    print("BMI: {0:.2f}".format(bmi)) 
    print("person is normal ")
else:
    print("BMI: {0:.2f}".format(bmi)) 
    print("person is overweight")


print (" ")
print ("Scott Partacz")
print ("Date:",time.strftime("%x"))
print ("Current time:",time.strftime("%X"))
