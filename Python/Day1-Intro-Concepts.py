#This is a single line comment

"""This is 
        multi line
            comment"""

#Print() function with examples
#We can use print function to output to screen
print("Hello World!")
print("show this in the console")
print("How are you?, It's nice to meet you!")

# Variables are containers that hold any values, such as string, num, float, etc..
my_name= "Bhanu"
my_age = 15
my_fav_sport="Cricket"
sum = 1 + 2 # 3
product = sum * 2

# you can output your variable using print like this
print(product)
print("My Name is:",my_name,", I'm ",my_age,"years old and I love watching or playing",my_fav_sport)


# Data types

''' A variable assumes a data type. Here are a few that you're likely to encounter:

        Numeric type	Number, with or without decimals	int, float, complex, no = 3
        Text type	    String of characters	            str = "a literal string"
        Boolean type	Boolean	                            continue = True

'''
#Examples
planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string

print(type(distance_to_alpha_centauri)) #returns "<class 'float'>"
