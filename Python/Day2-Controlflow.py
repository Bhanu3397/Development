'''
To express conditional logic in Python, you use if statements. When you're writing an if statement, you're relying on another concept we cover in this module, mathematical operators. Python supports the common logic operators from math: equals, not equals, less than, less than or equal to, greater than, and greater than or equal to. You're probably used to seeing these operators displayed using symbols, which is how they’re represented in Python, too.

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

'''

a = 97
b = 55
# test expression
if a < b:
    # statement to be run
    print(b)

'''
You use an if statement if you want to run code only if a certain condition is satisfied. The syntax of an if statement is always:
if test_expression:
    # statement(s) to be run

In Python, the body of an if statement must be indented.
'''

x = 20
y = 20
# Write the first if statement here:
if x==y:
  print("These numbers are the same")
credits = 120
# Write the second if statement here:
if credits >= 120:
  print("You have enough credits to graduate!")


# Boolean Operators: and 

'''
Often, the conditions you want to check in your conditional statement will require more than one boolean expression to cover. In these cases, you can build larger boolean expressions using boolean operators. These operators (also known as logical operators) combine smaller boolean expressions into larger boolean expressions.

There are three boolean operators are:
and
or
not

'''
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

credits = 120
gpa = 3.4
if credits >= 120 and gpa >= 2.0:
  print("You meet the requirements to graduate!")

#Boolean Operators: or
#The boolean operator or combines two expressions into a larger expression that is True if either component is True.
statement_one = (2 - 1 > 3) or (-5 * 2 == -10)
statement_two = (9 + 5 <= 15) or (7 != 4 + 3)
credits = 118
gpa = 2.0
if credits >= 120 or gpa >= 2.0:
  print("You have met at least one of the requirements.")

#Boolean Operators: not
'''
The final boolean operator we will cover is not. This operator is straightforward: when applied to any boolean expression it reverses the boolean value. So if we have a True statement and apply a not operator we get a False statement.

'''
statement_one = not (4 + 5 <= 9)
statement_two = not (8 * 2) != 20 - 4

credits = 120
gpa = 1.8
if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")
if not credits >= 120:
  print("You do not have enough credits to graduate.")
if not gpa>=2.0 and not credits >= 120:
  print("You do not meet either requirement to graduate!")