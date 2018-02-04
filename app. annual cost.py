# Scott Partacz 1/25/2018 ITMD 413 Lab 1
#gets the total number of appliances
import time
number_of_appliances = int(input("How many appliances? "))
#total cost
total_cost = 0
# used for the while loop
count = 0

while (count < number_of_appliances):
    print (" ")
    appliance_name = input("please enter the appliance name: ")
    cost_per_kw = float(input("please enter the cost per KW - hr of the appliance (in cents)): "))
    annual_usage = int(input("please enter the annual usage (in KW - hr): "))
    #adds to the total cost
    total_cost += cost_per_kw * annual_usage
    count += 1

print (" ")
# prints out a formatted value of total_cost
print ("The total cost of the annual usage is: $",format(total_cost,",.2f"))
#Name,Date,time
print (" ")
print ("Scott Partacz")
print ("Date:",time.strftime("%x"))
print ("Current time:",time.strftime("%X"))
