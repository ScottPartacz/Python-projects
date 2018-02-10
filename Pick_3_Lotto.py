# Scott Partacz 1/25/2018 ITMD 413 Lab 3
import time
import random

def check (picked,wining_numbers) :
    if(wining_numbers == picked) :
        win_or_lose = True
    elif(wining_numbers != picked) :
        win_or_lose = False
    return win_or_lose;

def fireball_check(fireball,picked,wining_numbers) :
    count = 0;
    temp1 = sorted([fireball,picked[1],picked[2]])
    temp2 = sorted([fireball,picked[0],picked[2]])
    temp3 = sorted([fireball,picked[0],picked[1]])
    #checks to see if the fireball would make the numbers a match
    if(temp1 == wining_numbers) :
        count += 1
    if(temp2 == wining_numbers) :
        count += 1
    if(temp3 == wining_numbers) :
        count += 1
    return count

fireball_wining = 0
fireball_flag = input("do you want to play fireball? (enter y/n) ")

list = sorted(random.sample(range(0, 10), 3))
fireball = random.randint(0,10)

#this is used to check the program is working
print(list,fireball);

while(True) :
    print("Plese enter your 3 numbers sperated by a space")
    numbers = [int(x) for x in input().split()]
    numbers.sort()
    
    # checks if you entered 3 numbers
    if(len(numbers) != 3) :
        print("\nError: 3 numbers were not entered")
        continue
    
    # checks if the numbers pick are between 0-9
    elif((numbers[0] > 9 or numbers[0] < 0) or (numbers[1] > 9 or numbers[1] < 0) or (numbers[2] > 9 or numbers[2] < 0)) :
        print("\nError: one of the numebrs entered wasnt 0-9")
        continue
    break
if(fireball_flag == "y") :
    fireball_wining = fireball_check(fireball,numbers,list)
    
flag = check(numbers,list)
# checks the lotto result
if ((flag == True) and fireball_wining > 0) :
    print("\nyou won $100 dollar cash prize and firball won too so an extra $50 times ",fireball_wining)
elif ((flag == False) and fireball_wining > 0) :
    print("\nyou lost but since you had fireball you win $50 times ",fireball_wining)
elif (flag == True) :
    print("\nyou win $100 dollar cash prize will be sent your way soon")
elif (flag == False) :
    print("\nNice try, better luck next time ")
    

print("\nThe wining numbers were: ",end =" ")
print(list)
print("\nThe Fireball number was: ",end =" ")
print(fireball)


print (" ")
print ("Scott Partacz")
print ("Date:",time.strftime("%x"))
print ("Current time:",time.strftime("%X"))
