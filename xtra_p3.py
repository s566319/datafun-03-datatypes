"""

Author: Inga Miller
44-608, Fundamentals of Data Analytics 
Project 3
Date: May 27, 2023


Purpose of this section is Optional bonus. 


>>> len(longwordset1)
415

>>> len(longwordset2)
197

>>> len(longwords)
13
"""

import doctest
import math


# TODO: import from local util_datafun_logger.py 

from util_datafun_logger import setup_logger

# TODO: Call the setup_logger function to create a logger and get the log file name

logger, logname = setup_logger(__file__)

def compare_two_plays():
    ''' This function compares two plays by Shakespeare.'''
    logger.info("Calling compare_two_plays()")
        
    # read from file and get a list of words

    with open("text_hamlet.txt", "r") as f1:
        text = f1.read()
        wordlist1 = text.split()  # split on whitespace

    logger.info(f"List of words from play 1: {wordlist1}")


    # read from file and get a list of words

    with open("text_hamlet.txt", "r") as f1:
        text = f1.read()
        wordlist1 = text.split()  #split on whitespace

    with open("text_juliuscaesar.txt", "r") as f2:
        text = f2.read()
        wordlist2 = text.split()  # split on whitespace

    logger.info(f"List of words from play 2: {wordlist2}")


    # Done with files - let the files close and the work begin

    # Remove duplicates by creating two sorted set

    # hint: use sorted() to sort the list
    # hint: use set() to remove duplicates
    # name them wordset1 and wordset2
    wordset1 = set(wordlist1)
    wordset2 = set(wordlist2)
    


    # initialize a variable maxlen = 10
    maxlen = 10

    # use a list comprension to get a list of words longer than 10

    # for word in wordset1
    # That is:
    # in a list (e.g. square brackets)
    # say "[Give me word (for each word in wordset1)
    #      if len(word) is greater than maxlen]"
    # then convert the list to a set to we can take the intersection
    # hint: use set()
    # name them longwordset1 and longwordset2
    longwordset1 = set([word for word in wordset1 if len(word) > 10])
    longwordset2 = set([word for word in wordset2 if len(word) > 10])

    # find the intersection of the two sets
    # that is, the words in both longwordset1 1 & longwordset2
    # name this variable longwords
    longwords = longwordset1 & longwordset2

    # print the length of the sets and the list
    print()
    print(f'Number of words in Hamlet with over 10 letters: {len(longwordset1)}')
    print(f'Number of words in Julius Caesar with over 10 letters: {len(longwordset2)}')
    print(f'Number of 10+ letter words in Hamlet and Julius Caesar: {len(longwords)}')
    print()
    print(f"Unique 10+ letter words in Hamlet and Julius Caesar: {sorted(longwords)}")
    print()
    
    # check your work
    print("TESTING...if nothing prints before the testing is done, you passed!")
    doctest.testmod()
    print("TESTING DONE")

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# -------------------------------------------------------------
# Call some functions and execute code!

if __name__ == "__main__":
    logger.info("Calling functions from main block")

    compare_two_plays()

    logger.info("Complete the code to compare two plays.")
    show_log()

# ignore this, added this to this to show changes/ 
# have something to commit, to show log file added

logger.info("Explore some functions in the math module")
logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
logger.info(f"math.perm(5,1) = {math.perm(5,1)}")


if __name__ == "__main__":

    logger.info("Explore some functions in the math module")
    logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
    logger.info(f"math.perm(5,1) = {math.perm(5,1)}")
    logger.info(f"math.comb(5,3) = {math.comb(5,3)}")
    logger.info(f"math.perm(5,3) = {math.perm(5,3)}")
    logger.info(f"math.pi = {math.pi}")
    logger.info(f"math.degrees(2 * math.pi) = {math.degrees(2 * math.pi)}")
    logger.info(f"math.radians(180)         = {math.radians(180)}")
    logger.info("")