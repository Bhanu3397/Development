#Operators
#Operators let you perform various operations on variables and their values. 
#The general idea is that you have a left side and a right side and an operator in the middle.

'''
Arithmetic operators

Type	Description	                                                                            Example
+	  Addition operator that adds two values together	                                        1 + 1
-	  Subtraction operator that removes the value of the right side from the left side	        1 - 2
/	  Division operator that divides the left side as many times as the right side specifies	10 / 2
*	  Multiplication operator	                                                                2 * 2

Assignment operators
You can use assignment operators to assign values to a variable throughout the lifecycle of the variable. 

Operator	Example
=	        x = 2
                    x now contains 2.
+=	        x += 2
                    x incremented by 2. If it contained 2 before, it now has a value of 4.
-=	        x -= 2
                    x decremented by 2. If it contained 2 before, it now has a value of 0.
/=	        x /= 2
                    x divided by 2. If it contained 2 before, it now has a value of 1.
*=	        x *= 2
                    x multiplied by 2. If it contained 2 before, it now has a value of 4.

'''

#Example
left_side = 10
right_side = 5
print(left_side / right_side) # 2


'''
Dates:

    When you're building programs, you're likely to interact with dates. A date in a program usually means both the calendar date and the time.

    You can use a date in various applications, like these examples:

    Backup file: Using a date as part of a backup file's name is a good way to indicate when a backup was made and when it needs to be  made again.
    
    Condition:. You might want to carry a specific logic when there's a certain date.
    
    Metric:. Dates are used to check performance on code to (for example) measure the time it takes to execute a function.
'''

#To work with a date, you need to import the date module

from datetime import date
date.today()
print(date.today())

#Data type conversion:

'''
You want to use a date with something, usually a string. If you, for example, want to show today's date on the console, you might run into a problem:

'''

#print("Today's date is: " + date.today()) # outputs error, beacause we are trying to combine a string and a date 

print("Today's date is: " + str(date.today())) # Here we are converting date to string with str()

parsecs = 11 
print(type(parsecs))
lightyears=parsecs*3.26
print(type(lightyears))
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")

#User input

'''
Another way to pass data to the program is having the user enter the data. You can code it so the program tells the user to enter information. You save that entered data in the program and then act on it.

'''
print("Welcome to the greeter program")
name = input("Enter your name ")
print("Greetings: " + name)

print("calculator program")
first_number = input("first number: ")
second_number = input("second number: ")
print(first_number + second_number) #Here + working as concatenate

print(int(first_number) + int(second_number)) # here it is working as addition

parsecs_input = input("Input number of parsecs:")
parsecs = int(parsecs_input)
lightyears = 3.26156 * parsecs

print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears")
