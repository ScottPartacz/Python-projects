# Scott Partacz 1/25/2018 ITMD 413 Lab 5

import time
import os
import sys

def menu() :
   pstr = "Choose from the following payroll choices\n"
   pstr += "(1) A gross PR payroll report for all employees\n"
   pstr += "(2) A gross PR payroll report for a single employee by name\n"
   pstr += "(3) Add an employee\n"
   pstr += "(4) Delete an employee\n"
   pstr += "(5) Modify an employee\n"
   pstr += "(6) Quit Program"
   print (pstr)

def printall() :
   if(os.path.exists("employees.txt")) :
       empFile = open("employees.txt", "r")
       answer = ""
       for line in empFile :
            answer = line
            print (answer)
       empFile.close()
   else :
       print("File not Found")
   

def printEmp() :
   if(os.path.exists("employees.txt")) :
       empFile = open("employees.txt", "r")
       line1 = empFile.readline()
       number_lines = sum(1 for line in open("employees.txt"))
       answer = ""
       count = 0
       name = input("Enter in a name to search employee ")
       while(line1 != "") :
           if (name == line1.split()[0] + " " + line1.split()[1]) :
               print("")
               print(line1)
               break
           if (count == number_lines - 1) :
               print("record not found")
           line1 = empFile.readline()
           count = count + 1
       empFile.close()
   else :
       print("File not Found") 

def addEmp() :
   if(os.path.exists("employees.txt")) :
       fname = input("Enter in your first name: ")
       lname = input("Enter in your last name: ")
       rate = input("Enter in your rate of pay: ")
       hours = input("Enter in the number of hours you worked: ")
       empFile = open("employees.txt", "a")
       empFile.write("\n" + fname + " " + lname + " " + rate + " " + hours)
       empFile.close()
   else :
       print("File not Found")

def deleteEmp() :
    if(os.path.exists("employees.txt")) :
       empFile = open("employees.txt", "r+")
       lines = empFile.readlines()
       number_lines = sum(1 for line in open("employees.txt"))
       answer = ""
       count = 0
       name = input("Enter in a name to delete ")
       empFile.seek(0)
       for i in lines:
           if name != i.split()[0] + " " + i.split()[1]:
              empFile.write(i)
              count += 1
       empFile.truncate()
       if(count == number_lines) :
           print("record not found")
    else :
       print("File not Found") 
def modifyEmp() :
    if(os.path.exists("employees.txt")) :
       empFile = open("employees.txt", "r+")
       lines = empFile.readlines()
       number_lines = sum(1 for line in open("employees.txt"))
       answer = ""
       count = 0
       empFile.seek(0)
       name = input("Enter in a name to modify ")
       for i in lines:
           if name != i.split()[0] + " " + i.split()[1]:
               count += 1
       if(count == number_lines) :
           print("record not found")
       else :
           empFile.seek(0)
           rate_change = input("Please enter the change in rate of pay (if no change leave blank): ")
           hour_change = input ("Please enter the change in hours worked (if no change leave blank): ")
           for i in lines:
               if name == i.split()[0] + " " + i.split()[1]:
                   if(rate_change == "") :
                      empFile.write(name + " " + i.split()[2] + " " + hour_change + "\n")
                   elif(hour_change == "") :
                       empFile.write(name + " " + rate_change + " " + i.split()[3] + "\n")
                   else :
                       empFile.write(name + " " + rate_change + " " + hour_change + "\n")
               else :
                   empFile.write(i)
           empFile.truncate()
    else :
       print("File not Found") 
def exitApp() :
   print("Exiting Program") 
   sys.exit()

def main() :
   while(True) :
       print("")
       menu()
       choice = int(input("Enter Menu Choice Now! "))
       print("")
       if choice == 1 : printall()
       if choice == 2 : printEmp()
       if choice == 3 : addEmp() 
       if choice == 4 : deleteEmp() 
       if choice == 5 : modifyEmp()
       if choice == 6 : exitApp() 
  

main()

#Name,Date,time
print (" ")
print ("Scott Partacz")
print ("Date:",time.strftime("%x"))
print ("Current time:",time.strftime("%X"))
