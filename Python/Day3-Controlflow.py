#Else Statements:
'''
else statements allow us to elegantly describe what we want our code to do when certain conditions are not met.
else statements always appear in conjunction with if statements. 
You know that when you use an if statement, the body of the program will run only if the test expression is True. To add more code that will run when your test expression is False, you need to add an else statement.

Ex:
if test_expression:
    # statement(s) to be run
else:
    # statement(s) to be run
'''

credits = 120
gpa = 1.9
if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
  print("You do not meet the requirements to graduate.")

a = 93
b = 27
if a >= b:
    print(a)
else:
    print(b)

#Else If Statements:
'''
In Python, the keyword elif is short for else if. An elif statement checks another condition after the previous if statements conditions aren’t met.

Using elif statements enables you to add multiple test expressions to your program. These statements run in the order in which they're written, so your program will enter an elif statement only if the first if statement is False. 

if test_expression:
    # statement(s) to be run
elif test_expression:
    # statement(s) to be run

'''
a = 93
b = 27
if a >= b:
    print("a is greater than or equal to b")
elif a == b:
    print("a is equal to b")

#Combine if, elif, and else statements:

'''
You can combine if, elif, and else statements to create programs with complex conditional logic. Remember that an elif statement is run only when the if condition is false. Also note that an if block can have only one else block, but it can have multiple elif blocks.

Ex:
if test_expression:
    # statement(s) to be run
elif test_expression:
    # statement(s) to be run
elif test_expression:
    # statement(s) to be run
else:
    # statement(s) to be run
'''

a = 93
b = 27
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else: 
    print ("a is equal to b")

grade = 86
if grade >= 90:
  print("A")
elif grade >=80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")


#Work with nested conditional logic:
'''
Python also supports nested conditional logic, meaning that you can nest if, elif, and else statements to create even more complex programs. To nest conditions, indent the inner conditions, and everything at the same level of indentation will be run in the same code block

if test_expression:
    # statement(s) to be run
    if test_expression:
        # statement(s) to be run
    else: 
        # statement(s) to be run
elif test_expression:
    # statement(s) to be run
    if test_expression:
        # statement(s) to be run
    else: 
        # statement(s) to be run
else:
    # statement(s) to be run

'''
a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")

