'''
As a developer, you'll frequently work with sets of data. You might need to manage multiple names, ages, or addresses. Storing each value in an individual variable makes code harder to read and write. To store multiple values, you can use a Python list.

Python has many built-in types, such as strings and integers. Python has a type for storing a collection of values: the list.
'''
#Empty list:
my_empty_list = []
#Create a list:
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

#Access list items by index:
'''You can access any item in a list by putting the index in brackets [] after the list variable's name. Indexes start from 0, so in the following code, planets[0] is the first item in the list planets:
'''
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

# Output
# The first planet is Mercury
# The second planet is Venus
# The third planet is Earth

#You can also modify list using an index
planets[3] = "Red Planet"
print("Mars is also known as", planets[3])

# Output
# Mars is also known as Red Planet

#Determine the length of a list:
number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")

# Output:
# There are 8 planets in the solar system

# Add values to lists:
'''Lists in Python are dynamic: you can add and remove items after they're created. To add an item to a list, use the method .append(value).'''
planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")

# Output:
# There are actually 9 planets in the solar system.

#Remove values from lists
'''You can remove the last item in a list by calling the .pop() method on the list variable.'''
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")

'''you can remove an item from list using index also'''
# Your code below:
garden_waitlist=["Jiho","Adam","Sonny","Alisha"]
garden_waitlist[1]='Calla'
print(garden_waitlist)
garden_waitlist[-1] = "Alex"
print(garden_waitlist)

'''You can use .remove() function to remove desired items from list'''
# Your code below: 
order_list=["Celery", "Orange Juice", "Orange", "Flatbread"]
print(order_list)
order_list.remove("Flatbread")
print(order_list)
new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
print(new_store_order_list)
new_store_order_list.remove("Mango")
print(new_store_order_list)
# new_store_order_list.remove("Onions") #Outputs error because Onions are not in the list

# Use negative indexes:
print("The first planet is", planets[0])

# Output:
# The first planet is Mercury

'''Indexes start at zero and increase. Negative indexes start at the end of the list and work backward.'''
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

# Output
# The last planet is Neptune
# The penultimate planet is Uranus

#Find a value in a list:
'''To determine where in a list a value is stored, you use the list's index method. This method searches for the value and returns the index of that item in the list. If it doesn't find a match, it returns -1.'''

jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")

# Output
# Jupiter is the 5 planet from the sun

#Growing a List: Plus (+):
items_sold = ["cake", "cookie", "bread"]
items_sold_new = items_sold + ["biscuit", "tart"]
print(items_sold_new)

my_list = [1, 2, 3]
# my_list + 4 #TypeError: can only concatenate list (not "int") to list

'''If we want to add a single element using +, we have to put it into a list with brackets ([]).'''
print(my_list + [4])
print(my_list) # [1,2,3]


#What can a List contain?
'''List can contains different types of data such as numbers(int,float), booleans(true,false), strings '''
my_data_list = ["data", 60, True, False, 6.0]
print(my_data_list)
print(" ")

#Two-Dimensional (2D) Lists:
'''We’ve seen that the items in a list can be numbers or strings. Lists can contain other lists! We will commonly refer to these as two-dimensional (2D) lists.'''
#Ex:
heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64]]
heights.append(["Vik",68])
ages = [["Aaron",15],["Dhruti",16]]

print(heights)
print(ages)

#Accessing 2D Lists:
class_name_test = [["Jenny",90],["Alexus",85.5],["Sam",83],["Ellie",101.5]]
print(class_name_test)
sams_score = class_name_test[2][1]
print(sams_score)
ellies_score=class_name_test[-1][-1] #using -ve index
print(ellies_score)

#Modifying 2D Lists:
#list contains name, country, grade.
incoming_class = [["Kenny","American",9],["Tanya","Russian",9],["Madison","Indian",7]]
print(incoming_class)
incoming_class[2][2]=8 #Changing madison grade to 8th.
print(incoming_class)
incoming_class[-3][-3]="Ken" #using -ve index to cahnge name
print(incoming_class)

#Use min() and max() with lists:
'''Python has built-in functions for calculating the biggest and smallest numbers in a list. The max() function returns the largest number, and min() returns the smallest. So min(gravity_on_planets) returns the smallest number in the gravity_on_planets list, which is 0.377 (Mars).'''

gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
print(min(gravity_on_planets))
print(max(gravity_on_planets))