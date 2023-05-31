"""

Author: Inga Miller
44-608, Fundamentals of Data Analytics 
Project 3
Date: May 27, 2023


Purpose of this section is to work with list statistics

"""""""""

import math
import statistics
"""
# Record your work automatically with our datafun logger
from util_datafun_logger import setup_logger
logger,logname = setup_logger(__file__)
"""
# TODO: import from local util_datafun_logger.py 

from util_datafun_logger import setup_logger

# TODO: Call the setup_logger function to create a logger and get the log file name

logger, logname = setup_logger(__file__)

# import some standard modules first - how many can you make use of?

import math
import statistics


# TODO: import from local util_datafun_logger.py 
from util_datafun_logger import setup_logger

# TODO: Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)

# TODO: Create some shared data lists if you like - or just create them in your functions

""""""

#list1 is a listing of number of visitors seen in Old Town Riga
# in one hour for several days in a row

""""""

List1 = [15, 21, 65, 50, 16, 30, 29, 41, 34, 23, 65, 32, 19, 18, 20, 32, 56, 87, 43, 44]

""""""
#listx represents 10 integer times

""""

listx = list(range(10))

"""
#listy represents the high temperature for the day the visitors are counted

"""

listy = [67, 87, 67, 69, 71, 75, 79, 81, 82, 80]

divider = "====================********=============================="

print("List 1. List Statistics")

""" 
#Calculate mean, median, mode, standard deviation, and variance
#for list1

"""

print()
mean = stats.mean(list1)
median = stats.median(list1)
mode = stats.mode(list1)
st_dev = stats.stdev(list1)
variance = stats.variance(list1)

print(f"Visitor Count Mean: {round(mean, 2)}")
print(f"Visitor Count Median: {round(median, 2)}")
print(f"Visitor Count Mode: {round(mode, 2)}")
print(f"Visitor Count Standard Deviation: {round(st_dev, 2)}")
print(f"Visitor Count Variance: {round(variance, 2)}")

print()
print(divider)
print()

print("Lists 2. Lists - Correlation and Prediction")

"""
#Calculate the correlation, slope, and intercept of the best fit
#line for listx and listy
#Predict the y value for future time x = 15
#Predict the y value at a future time y = mx + b where m is the slope and b is the y intercept

"""

print()
correlationxy = stats.correlation(listx, listy)
slope, intercept = stats.linear_regression(listx, listy)
xfuture = 15
yfuture = slope * xfuture + intercept

print(f"Correlation between time and weather temperature: {round(correlationxy, 2)}")
print(f"Slope of best-fit line for listx and listy: {round(slope, 2)}")
print(f"Intercept of best-fit line for listx and listy: {round(intercept, 2)}")
print(f"Predicted weather temperature at future time 15: {round(yfuture, 2)}")


print()
print(divider)
print()

print("List 3. Lists = Using Python Built-in Functions")

"""
#Calculate the min, max, length, sum, and average of list1
#Create a set from list1, and sort list1 in both forward 
#and reverse directions

"""
print()

count_min = min(list1)
count_max = max(list1)
count_length = len(list1)
count_sum = sum(list1)
count_avg = count_sum / count_length
count_set = set(list1)
count_sorted_for = sorted(list1)
count_sorted_back = sorted(list1, reverse=True)

print(f"Minimum Visitor Count: {count_min}")
print(f"Maximum Visitor Count: {count_max}")
print(f"Number of Counting Days: {count_length}")
print(f"Total Number of Visitors Counted: {count_sum}")
print(f"Average Number of Visitor per Count: {round(count_avg, 2)}")
print(f"Visitor Count Set: {count_set}")
print(f"Visitor Counts Sorted (Ascending): {count_sorted_for}")
print(f"Visitor Counts Sorted (Descending): {count_sorted_back}")

print()
print(divider)
print()

print("List 4. List Methods")

"""
#Create new short list and use list methods append, extend, 
#insert, remove number 5, count how many times 2 apprears, sort (forward and reverse), copy, and
#pop (first and last)

""""""

print()

# Create a new short list lst
lst = [9, 19, 29, 2, 5, 4, 5]
print(f"Lst: {lst}")

# Append a a single value
lst.append(2)
print(f"Appended lst: {lst}")

# Extend list with new list
lst.extend([15, 5, 95])
print(f"Extended lst: {lst}")

# Insert a value at index 4
lst.insert(10, 4)
print(f"lst With Insert: {lst}")

# Remove number 5 from list
lst.remove(5)
print(f"List Minus Value 5: {lst}")

# Count how many times number 2 appears in lst
print(f"The value 2 appears {lst.count(2)} times in lst.")

# Sort list
lst.sort()
print(f"lst Sorted in Ascending Order: {lst}")

# Sort list reversed
lst.sort(reverse=True)
print(f"lst Sorted in Descending Order: {lst}")

# Create a copy of list
lst_copy = lst.copy()
print(f"Copy of lst: {lst_copy}")

# Pop the first item off the top of the list
first = lst.pop(0)
print(f"lst First Value Popped: {first}")

# Pop the last item off the bottom of the list
last = lst.pop(-1)
print(f"lst Last Value Popped: {last}")


print("List 5. List Transformations - Using filter() and map()")

#use the built in filter () function to keep x such that x is less than 4

print()

""""""

#use the built in map() to map each x cuberoot of x

#dont know how to do this

#use the built in map() to calculate the volume of cube

#dont know how to do this
  # Use the built-in function filter() anywhere you need to filter a list
    # Filter the new list to only include scores greater than 100
    # You could pass in a named function, but honestly this is easier
    # Say "KEEP x such that x > 100 is True" given score_list
    # Cast the result using square brackets to get back a list

    # Use the built-in function map() anywhere you need to transform a list

    # Map each element to its square
    # Say "map x to x squared" given score_list
    # Cast the result using square brackets to get a list
  

    # Map each element to its square root
    # Say "map x to the square root of x" given score_list
    # remember to cast the result to a list (using square brackets)
   
    # Map each element (radius) to its area
    
    # Say "map r to pi r squared" given radius_list
    # cast the result to a list using square brackets
 

print("Lists 6. List Transformations - Using List Comprehension")

#dont know how to do this

print()

# Use a list comprehension to triple each value on list1

#dont know how to do this

print()

# Convert each temperature into Celsius

#dont know how to do this

print()

logger.info("Explore some functions in the math module")
logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
logger.info(f"math.perm(5,1) = {math.perm(5,1)}")


