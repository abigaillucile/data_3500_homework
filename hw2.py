#2.3
# ask user to input grade
grade = float(input("What is your grade in the class (as a percent)? "))
if grade >= 90: #determine if they got an A
    print(f"Congratulations!! Your grade of {grade}% earned you an 'A' in the class!!")
    

#2.4
# calculate equations
print("27.5 + 2:", 27.5 + 2)
print("27.5 - 2:", 27.5 - 2)
print("27.5 * 2:", 27.5 * 2)
print("27.5 / 2:", 27.5 / 2)
print("27.5 // 2:", 27.5 // 2)
print("27.5 ** 2:", 27.5 ** 2)

#2.5
pi = 3.14159 #declare pi var
r = 2 #declare raidus var
# calculations
print("Diameter:", 2*r)
print("Circumference:", 2*pi*r)
print("Area:", pi*(r**2))

2.6
#ask user to give a number
integer = eval(input("Please input your favorite number: "))
#Determine if it is even or odd
if integer%2 == 0:
    print("Your number is even!")
else: 
    print("Your number is odd!")

2.7
# declare num var
num1 = 1024
num2 = 2
#test if 1024 a multiple of 4
if 1024 % 4 != 0: 
    print("Sorry! 1024 is not a multiple of 4.")
else: 
    print("Perfect! 1024 is a multiple of 4!")
# test if 2 is a multiple of 10
if 2 % 10 != 0: 
    print("Sorry! 2 is not a multiple of 10.")
else: 
    print("Perfect! 2 is a multiple of 10!")

2.8
print("number\tsquare\tcube") #initial format
for i in range (6): #create range
    number = i
    square = i ** 2
    cube = i ** 3
    print(f"{number}\t{square}\t{cube}")
