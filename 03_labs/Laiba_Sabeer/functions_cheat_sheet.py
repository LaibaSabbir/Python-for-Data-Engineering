# Author: Laiba Sabeer
# Date: 2025-10-21

#######################################################################
##########STRINGS##########

#Python String .format()
# The Python string method .format() replaces empty brace ({}) placeholders in the string with its arguments.
# If keywords are specified within the placeholders, they are replaced with the corresponding named arguments to the method.
msg1 = 'Fred scored {} out of {} points.'
print(msg1.format(3, 10))   # => 'Fred scored 3 out of 10 points.'

msg2 = 'Fred {verb} a {adjective} {noun}.'
print(msg2.format(adjective='fluffy', verb='tickled', noun='hamster')) # => 'Fred tickled a fluffy hamster.'


# String Method .lower()
# The string method .lower() returns a string with all uppercase characters converted into lowercase.
greeting = "Welcome To Chili's"
print(greeting.lower())  # Prints: welcome to chili's


# String Method .upper()
# The string method .upper() returns the string with all lowercase characters converted to uppercase.
dinosaur = "T-Rex"
print(dinosaur.upper())   # Prints: T-REX


#String Method .strip()
# The string method .strip() can be used to remove characters from the beginning and end of a string.
# A string argument can be passed to the method, specifying the set of characters to be stripped. With no arguments to the method, whitespace is removed.
text1 = '   apples and oranges   '
print(text1.strip() )      # => 'apples and oranges'

text2 = '...+...lemons and limes...-...'
print(text2.strip('.') )   # => '+...lemons and limes...-'
print(text2.strip('.+') )  # => 'lemons and limes...-'
print(text2.strip('.+-'))  # => 'lemons and limes'


# .find()
# The Python string method .find() returns the index of the first occurrence of the string passed as the argument. It returns -1 if no occurrence is found.
mountain_name = "Mount Kilimanjaro"
print(mountain_name.find("o")) # Prints 1 in the console.


# "in" function
# The in syntax is used to determine if a letter or a substring exists in a string. It returns True if a match is found, otherwise False is returned.
game = "Popular Game: Mario Kart"

print("l" in game) # Prints: True
print("x" in game) # Prints: False

# String replace
# The .replace() method is used to replace the occurence of the first argument with the second argument within the string.
fruit = "Strawberry"
print(fruit.replace('r', 'R'))  # StRawbeRRy


# String Method .join()
# The string method .join() concatenates a list of strings together to create a new string joined with the desired delimiter.
x = "-".join(["Hello", "world"])
print(x) # Prints: Hello-world

x = "".join(["Hello", "world"])
print(x) # Prints: Helloworld


# Escaping Characters
# Backslashes (\) are used to escape characters in a Python string.
txt = "She said \"Never let go\"."
print(txt) # She said "Never let go".


# Indexing and Slicing Strings
# Python strings can be indexed using the same notation as lists, since strings are lists of characters. A single character can be accessed with bracket notation ([index]), or a substring can be accessed using slicing ([start:end]).
# Indexing with negative numbers counts from the end of the string.
str = 'yellow'
print(str[1] )    # => 'e'
print(str[-1] )   # => 'w'
print(str[4:6] )  # => 'ow'
print(str[:4]  )  # => 'yell'
print(str[-3:] )  # => 'low'


# Iterate String
# To iterate through a string in Python, “for…in” notation is used.
str = "hello"
for c in str:
  print(c)


# len() Function 
# In Python, the built-in len() function can be used to determine the length of an object. It can be used to compute the length of strings, lists, sets, and other countable objects.
length = len("Hello")
print(length) # Output: 5

colors = ['red', 'yellow', 'green']
print(len(colors)) # Output: 3


# String Concatenation
# To combine the content of two strings into a single string, Python provides the + operator. This process of joining strings is called concatenation.
x = 'One fish, '
y = 'two fish.'
z = x + y
print(z)  # Output: One fish, two fish.


# IndexError
# When indexing into a string in Python, if you try to access an index that doesn’t exist, an IndexError is generated. For example, the following code would create an IndexError:
fruit = "Berry"
#print(fruit[6])


#######################################################################
##########INTEGERS##########

# Absolute Value
# The built-in function abs() will return the absolute value of a number that you pass to it.
print(abs(-4544))	#4544


# Power
# In Python, you can use the operator ** to raise a number by an exponent, or you can use the built-in function pow() which takes in two numbers.
print(pow(2,4))

# Rounding Numbers
# The built-in Python function round() takes in two numbers, one to be rounded, and one that specifies the number of decimal places to include.
i = 17.34989436516001
print(round(i,4))


# Calculating a Sum
# The sum() function is used for calculating sums of numeric compound data types, including lists, tuples, and dictionaries.
some_floats = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
print(sum(some_floats))

print(sum((8,16,64,512)))	# Calculate sum of numbers in tuple
print(sum({-10: 'x', -20: 'y', -30: 'z'}))	# Calculate sum of numbers in dictionary

# The sum() function can take up to 2 arguments, so you can add an additional number in integer or float form to add to the numbers that make up the argument in the first position:
some_floats = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]

print(sum(some_floats, 0.5))
print(sum({-10: 'x', -20: 'y', -30: 'z'},50))


#######################################################################
##########DATE TIME##########
import datetime 
from datetime import date 

current_time = datetime.datetime.now() 
print("Current Date and Time:", current_time) 


d = date(2025, 5, 2) 
print(d)   #2025-05-02 

from datetime import time 
#It represents a time of day (hour, minute, second, microsecond). The syntax of the time class is as follows:
# datetime.time(hour=0, minute=0, second=0, microsecond=0) 

t = time(14, 30) 
print(t) 

from datetime import datetime 
# Combines both date and time into a single object. The syntax of the datetime class is as follows:
# datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0) 

dt = datetime(2025, 5, 2, 14, 30) 
print(dt) 

from datetime import datetime, timedelta 
# The timedelta class represents a duration, i.e., the difference between two dates or times. It performs arithmetic with date, time, or datetime objects. The syntax of the timedelta class is as follows:
# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

start = datetime(2025, 5, 2) 
duration = timedelta(days=10) 
end = start + duration 
print("End date:", end) 

date1 = datetime(2025, 5, 12) 
date2 = datetime(2025, 5, 2) 
difference = date1 - date2 
print("Difference in days:", difference.days) 

from datetime import datetime 

# The strftime() method generates a string representation of a date, time, or datetime object using a specified format.
now = datetime(2025, 5, 2, 14, 30) 
formatted = now.strftime("%Y-%m-%d %H:%M:%S") 
print(formatted) 

#Use the strptime() method from the datetime class:
date_str = "2025-05-02"  
dt = datetime.strptime(date_str, "%Y-%m-%d")  
print(dt)


# How to compare two dates in Python?
# Two datetime or date objects can be compared directly using comparison operators like ==, <, >, etc.

from datetime import date 

d1 = date(2025, 5, 2) 
d2 = date(2025, 5, 10) 
print(d1 < d2)