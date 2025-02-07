#3.4
for x in range(2): #start loop
    for y in range(7):
        print('@ ', end='') #format
    print()#start second row



#3.9
while(True): #start loop to check condiditons
    #declare variables and ask fo rinput 
    digit = input("Please enter a 7-10 digit number: ")
    length = len(digit)
    digit = int(digit)
        #and.... is it the right length???
    if length > 6 and length < 11:
        print("Your digit is:")
        for x in range(length-1, -1, -1): #loop it!!!
            printNum = (digit // (10 ** x)) % 10 #the math that took me forever to figure out but now i understand! 
            print(printNum)
        break
    else: #If not... I should have more fun with this output but oh well im tired! :)
        print("That is not the correct length of digits. Please try again.")



#3.11
#declare variable for addition
galTotal = 0 
milesTotal = 0
#declare variable to track how many times they filled up the tank 
count = 0
#declare sentinal var
track = 0
#The while loop will go here... eventually
while track == 0:
#ask for the miles dirven and ask for the gallons per tankful
    miles       = float(input("Enter miles driven (inpute '-1' to end): "))
    if miles == -1: 
        track = 1
    else: 
        gallons     = float(input("Enter the gallons used: "))
        milesTotal  += miles
        galTotal    += gallons
        count       += 1 #calc and display the miles per gallon (add them as you go to a sep var)
        #print loop calc
        print(f"The miles/gallon for this tank was {miles/gallons}")

#break from while loop and print avg 
print(f"The average miles/gallon is: {milesTotal/galTotal}.")





#3.12
#as for input
number = int(input("Enter a five digit number:"))

#declare variables
first_num   = number // 10000
last_num    = number % 10
second_num  = (number - first_num * 10000) // 1000
fourth_num  = ((number % 1000) % 100) // 10

#Test conditions
if first_num == last_num: 
    if second_num == fourth_num: 
        print("palindrome")
else: 
    print("That is not a palindrome")
    



#3.14
#numerator is always 4, denomonator is always odd and starts at 1
#declare vars
num = 4
den = 1
total = 0 

#loop 
for i in range(1, 3000+1):
    if i % 2 == 0: 
        total -= num/den
    elif i % 2 != 0: 
        total += num/den
    #total += num/den
    den += 2
    print("i:", i, "total:", total)
    #2454 and 2455








    