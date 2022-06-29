#About 'while' loops
print("About 'while' loops", end="\n\n")
'''When you write code, one common challenge is to have it perform a task an unknown number of times. In this unit, you want to allow a user to enter a list of planet names. Unfortunately, you don't know how many names the user will enter. To support looping an unknown number of times, you can use a while loop.

A while loop performs an operation while a certain condition is true. You could look to see if there's another line in a file, a flag has been set, a user has finished entering values, or something else has changed to indicate that the code can stop performing the operation.'''

'''The most important thing to remember when you create while loops is to ensure that the condition changes. If the condition is always true, Python will continue to run your code until the program crashes.'''

user_input = ''

while user_input.lower() != 'done':
    user_input = input('Enter a new value, or done when done: ')

# Create the variable for user input
user_input = ''
# Create the list to store the values
inputs = []

# The while loop
while user_input.lower() != 'done':
    # Check if there's a value in user_input
    if user_input:
        # Store the value in the list
        inputs.append(user_input)
    # Prompt for a new value
    user_input = input('Enter a new value, or done when done: ')
print(inputs, end="\n\n") #Prints list after while loop done

#Use 'for' loops with lists
print("Use 'for' loops with lists", end="\n\n")
'''Python lists are iterable, and they can be used with a for loop. You use a for loop with iterables where you'll loop a known number of times, once for each item in the iterable.'''

countdown = [4, 3, 2, 1, 0]
for number in countdown:
    print(number)
print("Blast off!! 🚀", end="\n\n")

from site import ENABLE_USER_SITE
from time import sleep
countdown = [4, 3, 2, 1, 0]
for number in countdown:
    print(number)
    sleep(1)  # Wait 1 second
print("Blast off!! 🚀",end="\n\n")

new_planet = ''
planets = []
while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Enter a new planet or done if done: ')
for planet in planets:
    print(planet)
print(' ')

#Introducing Python dictionaries
print("Introducing Python dictionaries", end= "\n\n")
'''Python uses curly braces ({ }) and the colon (:) to denote a dictionary. You can either create an empty dictionary and add values later, or populate it at creation time. Each key/value is separated by a colon, and the name of each key is contained in quotes as a string literal. Because the key is a string literal, you can use whatever name is appropriate to describe the value.'''

'''You have two keys, 'name' and 'moons'. Each of these behaves in much the same way as a variable: they have a unique name, and they store a value. However, they are contained inside of a single, larger variable, named planet.'''
planet = {
    'name': 'Earth',
    'moons': 1
}

#Read dictionary values
print("Read dictionary values", end="\n\n")
print(planet.get('name'),end="\n\n")

# planet['name'] is identical to using planet.get('name')
print(planet['name'], end="\n\n")

'''Although the behavior of get and the square brackets ([ ]) is generally the same for retrieving items, there is one key difference. If a key isn't available, get returns None, and [ ] raises a KeyError.'''

wibble = planet.get('wibble') # Returns None
# wibble = planet['wibble'] # Throws KeyError

#Modify dictionary values
print("Modify dictionary values", end="\n\n")

planet.update({'name': 'Makemake'}) # name is now set to Makemake
planet['name'] = 'Makemake' # name is now set to Makemake
print(planet, end="\n\n")

# Using update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})
# Using square brackets
planet['name'] = 'Jupiter'
planet['moons'] = 79
print(planet, end="\n\n")

#Add and remove keys
print("Add and remove keys", end="\n\n")
'''To remove a key, you use pop. pop returns the value and removes the key from the dictionary. To remove orbital period, you can use the following code:'''

planet['orbital period'] = 4333
# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
#   orbital period: 4333
# }
print(planet, end="\n\n")
planet.pop('orbital period')
# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
# }
print(planet, end="\n\n")

#Complex data types
print("Complex data types", end="\n\n")
print(planet, end="\n\n")

# Add address
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}
# planet dictionary now contains: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }
print(planet, end="\n\n")
print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}') # Output: Jupiter polar diameter: 133709