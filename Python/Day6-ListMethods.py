#Adding by Index: Insert
print("#Adding by Index using Insert",end="\n\n")
'''The Python list method .insert() allows us to add an element to a specific index in a list.'''
'''The .insert() method takes in two inputs:
1.The index you want to insert into.
2.The element you want to insert at the specified index.'''

front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list, end='\n\n')
 
front_display_list.insert(0,"Pineapple") #Adding pineapple to be the first item in list
print(front_display_list, end='\n\n')


#Removing by Index: Pop
print("#Removing by Index using Pop",end="\n\n")
'''Python gives us a method to remove elements at a specific index using a method called .pop().The method can be called without a specific index. Using .pop() without an index will remove whatever the last element of the list is. .pop() is unique in that it will return the value that was removed.'''

data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics,end='\n\n')

data_science_topics.pop()
print(data_science_topics,end='\n\n')

data_science_topics.pop(3)
print(data_science_topics,end='\n\n')

#Consecutive Lists: Range
print("Consecutive Lists: Range", end='\n\n')
'''range() creates a list starting at 0. However, if we call range() with two inputs, we can create a list that starts at a different number.range(2, 9, n) will give us a list where each number is n greater than the previous number'''
number_list = range(9)
print(number_list, end='\n\n')
number_list = range(3)
print(list(number_list),end='\n\n')

zero_to_seven = range(8)
print(list(zero_to_seven), end='\n\n')


range_five_three = range(5, 15, 3)
print(range_five_three, end='\n\n')
print(list(range_five_three), end='\n\n')

range_diff_five = range(0,40,5)
print(range_diff_five, end='\n\n')
print(list(range_diff_five), end='\n\n')

#Length
print("Length method in list",end="\n\n")
long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]
big_range = range(2, 3000, 10)
long_list_len = len(long_list)
print(long_list_len, end ="\n\n")
big_range_length = len(big_range)
print(big_range_length, end = "\n\n")
print(big_range_length, end = "\n\n")
big_range = range(2, 3000, 15)
big_range_length = len(big_range)
print(big_range_length, end = "\n\n")

#Manipulate list data
print("#Manipulate list data",end="\n\n")
#Slice lists:
print("Slicing Lists", end="\n\n")
'''You can retrieve a portion of a list by using a slice. A slice uses brackets, but instead of a single item, it has the starting and ending indexes. When you use a slice, you create a new list that starts at the starting index and that ends before (and does not include) the ending index.'''

'''The list of planets has eight items. Earth is the third in the list. To get the planets before Earth, use a slice to get items starting at 0 and ending at 2:'''
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:2]
print(planets_before_earth,end="\n\n")

planets_after_earth = planets[3:8]
print(planets_after_earth,end="\n\n") 

planets_after_earth = planets[3:]
print(planets_after_earth)

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
beginning = suitcase[0:2] # select first two items from suitcase list
print(beginning,end="\n\n")
middle= suitcase[2:4] # Select midlle two items from suitcase list
print(middle,end="\n\n")
last_two_elements = suitcase[-2:]
print(last_two_elements, end="\n\n")
slice_off_last_three = suitcase[:-3] #print all but the last three elements.
print(slice_off_last_three)

#Join lists:
print("Join lists:",end="\n\n")
'''To join two lists, you use the other operator (+) with two lists to return a new list'''
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

#Sort lists:
print("Sort lists:",end="\n\n")
'''To sort a list, use the .sort() method on the list. Python will sort a list of strings in alphabetical order and a list of numbers in numeric order:'''
regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons,end="\n\n")

#Sort lists in reverse
regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons,end="\n\n")

