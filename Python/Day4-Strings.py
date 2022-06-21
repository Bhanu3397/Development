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
