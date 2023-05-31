"""

Author: Inga Miller
44-608, Fundamentals of Data Analytics 
Project 3
Date: May 27, 2023


Purpose of this section is to work with Tuples and More.

"""

divider = "=======================••••••••••••••==========================="

print()
print("Working with Tuples")
print()

# TODO: import from local util_datafun_logger.py 

from util_datafun_logger import setup_logger

# TODO: Call the setup_logger function to create a logger and get the log file name

logger, logname = setup_logger(__file__)

# Tuples
June_random_temperatures = (69, 70, 84, 85, 69)
July_random_temperatures = (69, 70, 84, 85, 69)
August_random_temperaturs = (69, 70, 84, 85, 69)

print(f"June Random Temperatures: {June_random_temperatures}")
print(f"July Random Temperatures: {July_random_temperatures}")
print(f"August Random Temperatures: {August_random_temperaturs}")

print()

# Slice tuples
jun_morning = June_random_temperatures[:3]
jul_evening = July_random_temperatures[3:]

print(f"June Morning Slice: {jun_morning}")
print(f"July Evening Slice: {jul_evening}")

print()

# Concatenate tuples
summer_temperatures = June_random_temperatures + July_random_temperatures + August_random_temperaturs
print(f"Summer's temperatures: {summer_temperatures}")

print()

# Tuple repetition
three_jun = June_random_temperatures * 3
print(f"Triple June temperatures: {three_jun}")

print()


# Tuple Indexing
first_jun = June_random_temperatures[0]
last_jun = June_random_temperatures[-1]
print(f"June 1st temp was {first_jun}.")
print(f"June 30th temp was {last_jun}.")

# Unpacking tuples
first, second, third, fourth, fifth = August_random_temperaturs
print(
    f"""
August First: {first}
August Second: {second}
August Third: {third}
August Fourth: {fourth}
August Fifth: {fifth}
"""
)

print()
print(divider)
print()

print("Practicing With Sets")

print()

set1 = {"June", "July", "August", "June", "September", "October", "June"}
set2 = {"July", "July", "August", "October", "December","November"}
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

print()

union_set = set1 | set2
intersection_set = set1 & set2
print(f"The union of set 1 and set 2 is: {union_set}")
print(f"The intersection of set 1 and set 2 is: {intersection_set}")

print()
print(divider)
print()

print("Practicing With Dictionaries")

print()

with open("text_woodchuck.txt") as text:
    word_list = text.read().split()

word_counts_dict = {word: word_list.count(word) for word in word_list}
print(f"Word Counts in Woodchuck Text: {word_counts_dict}")

print()

