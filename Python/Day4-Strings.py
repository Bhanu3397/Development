#String basics in Python:
'''
In Python, strings are immutable. That is, they can't change. This property of the string type can be surprising, because Python doesn't give you errors when you alter strings.

'''
fact = "The Moon has no atmosphere."
print(fact) # prints fact value
print(fact+"No sound can be heard on the Moon.") #The Moon has no atmosphere.No sound can be heard on the Moon. But fact value does not change

two_facts = fact + "No sound can be heard on the Moon."
print(two_facts) #'The Moon has no atmosphere.No sound can be heard on the Moon.'

#About using quotation marks:
moon_radius = "The Moon has a radius of 1,080 miles"
# another way to write string 
# 'The "near side" is the part of the Moon that faces the Earth'
# "We only see about 60% of the Moon's surface"
# """We only see about 60% of the Moon's surface, this is known as the "near side"."""

#Multiline text:
# There are a few different ways to define multiple lines of text as a single variable. The most common ways are:
'''
Use a newline character (\n).
Use triple quotation marks (""").

'''
multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)
#output
'''
Facts about the Moon:
 There is no atmosphere.
 There is no sound.

'''
multiline = """Facts about the Moon:
...  There is no atmosphere.
...  There is no sound."""
print(multiline)
'''
output:
Facts about the Moon:
 There is no atmosphere.
 There is no sound

'''

#String methods in Python:

'''
String methods are part of the str type. This means that the methods exist as string variables, or part of the string directly. For example, the method .title() can be used with a string directly.

'''
"temperatures and facts about the moon".title() #'Temperatures And Facts About The Moon'

heading = "temperatures and facts about the moon"
heading.title() #'Temperatures And Facts About The Moon'

#Split a string:
temperatures = """Daylight: 260 F
... Nighttime: -280 F"""
temperatures .split()  #['Daylight:', '260', 'F', 'Nighttime:', '-280', 'F']

temperatures .split('\n') #['Daylight: 260 F', 'Nighttime: -280 F']
'''
This type of splitting becomes handy when you need a loop to process or extract information, or when you're loading data from a text file or another resource.

'''

#Search for a string:
'''
The simplest way to discover whether a given word, character, or group of characters exists in a string is without using a method:

'''
print("Moon" in "This text will describe facts and challenges with space travel") #False
print("Moon" in "This text will describe facts about the Moon") #True

'''
An approach to finding the position of a specific word in a string is to use the .find() method. The .find() method returns a -1 when the word isn't found, or it returns the index (the number representing the place in the string).

'''
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
... while Mars has -28 Celsius."""
temperatures.find("Moon") #-1

#This is how it would behave if you're searching for the word Mars
temperatures.find("Mars") #65

#Another way to search for content is to use the .count() method, which returns the total number of occurrences of a certain word in a string.
temperatures.count("Mars") #1
temperatures.count("Moon") #0

#you can convert a string to all lowercase letters by using the .lower() method.
"The Moon And The Earth".lower()
"The Moon And The Earth".upper()

#Check content:
temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts) #['Mars average temperature', ' -60 C']
parts[-1] #' -60 C'

#Like the .isnumeric() method, .isdecimal() can check for strings that look like decimals.
mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item) #30

print("-60".startswith('-')) #True

if "30 C".endswith("C"):
    print("This temperature is in Celsius") #'This temperature is in Celsius'

#Transform text:
print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))

text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text) #False
print("temperatures" in text.lower()) #True

moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year"]
print('\n'.join(moon_facts))

#String format in Python

#Percent sign (%) formatting:
'''The placeholder is %s, and the variable is passed onto the text after the % character outside the string. Here's how to format by using the % character.'''

mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth" % mass_percentage) #On the Moon, you would weigh about 1/6 of your weight on Earth

print(' ')

#Using multiple values changes the syntax, because it requires parentheses to surround the variables that are passed in:
print("""Both sides of the %s get the same amount of sunlight,
... but only one side is seen from %s because
... the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))

#The format() method:

#The .format() method uses braces ({}) as placeholders within a string, and it uses variable assignment for replacing text.

mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth".format(mass_percentage))
print(' ')
#You don't need to assign repeated variables multiple times, making it less verbose because fewer variables need to be assigned.
print("""You are lighter on the {0}, because on the {0} 
... you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))

'''
Instead of empty braces, the substitution is to use numbers. The {0} means to use the first (index of zero) argument to .format(), which in this case is Moon. For simple repetition {0} works well, but it reduces readability. To improve readability, use keyword arguments in .format() and then reference the same arguments within braces.

'''
print(' ')
print("""You are lighter on the {moon}, because on the {moon} 
... you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))
print(' ')
#About f-strings:
'''it's possible to use f-strings. These strings look like templates with the same named variables as those in code. Using f-strings in the preceding example would look like this:'''

print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth")
#The variables go within braces, and the string must use the f prefix
print(' ')

print(round(100/6, 1))

print(' ')
#With f-strings, you don't need to assign a value to a variable beforehand.
print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth")

print(' ')
subject = "interesting facts about the moon"
f"{subject.title()}" #'Interesting Facts About The Moon'
