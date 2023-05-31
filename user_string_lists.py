"""

Author: Inga Miller
44-608, Fundamentals of Data Analytics 
Project 3
Date: May 27, 2023


Purpose of this section is to work with string lists.

"""

# imports first
import random

# Record your work automatically with our datafun logger
from util_datafun_logger import setup_logger
logger,logname = setup_logger(__file__)

# lists of buildings in Old Town Riga and characteristics

buildings = ["The Freedom Monument", "House of Black Heads", "Riga Dome Cathedral", "St. Peter's Church", "Swedish Gate"]

hours_to_explore = ["1", "2", "2", "3", "1"]

main_color = ["red", "gray", "yellow", "orange", "black"]

size = ["small", "extra large", "medium", "small", "large"]

age = ["530", "521", "560", "580", "501"]

divider = "====================••••••••••••••••••====================="

print()
print("String Lists 1. Using Python Built-in Functions")

"""
Use len, set, and zip functions

"""

print()

# Use len function
print(f"The length of the buildings list is {len(buildings)}.")

# Use set function
print(f"The unique values in the main color list are {set(main_color)}.")

# Combine multiple lists with zip function
building_tuples = zip(buildings, main_color, age)
print(f"Tuples of buildings, color, and age: {list(building_tuples)}")

print()
print(divider)
print()

print("String Lists 2. Random Choice")

print()

print(f"Random choice from main color list: {random.choice(main_color)}")

randomized_sentence = (
    f"The {random.choice(buildings)} is a {random.choice(size)} building,"
    f"and the ages are {random.choice(age)}...... maybe not!"
)

print()

print(randomized_sentence)

print()
print(divider)
print()

print("String Lists 3. Get Unique Words")
"""
Use open(), read(), split(), and set() to create a list of unique
words from a provided text

"""

print()

with open("text_names_in.txt", "r") as file:
    text = file.read()
    list_words = text.split()
    unique_words = set(list_words)

unique_words_sorted = sorted(unique_words)
unique_word_count = len(unique_words_sorted)
print(f"Names contains {unique_word_count} unique words!")

print()

# ignore this, added this to show changes/ have something to commmit to show that I added log file