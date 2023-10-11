# You need to write a function, that returns the first non-repeated character in the given string.

# If all the characters are unique, return the first character of the string.
# If there is no unique character, return None.

# You can assume, that the input string has always non-zero length.

# Examples
# "test"   returns "e"
# "teeter" returns "r"
# "trend"  returns "t" (all the characters are unique)
# "aabbcc" returns None (all the characters are repeated)

from collections import Counter
# string = 'test'
def solution(string):
    counter = Counter(string)
    for k, v in counter.items():
        if v==1:
            return k
    return None

def solution(string):
    letter_count = {}
    for letter in string:
        if letter in letter_count:
            letter_count[letter] +=1
        else:
            letter_count[letter] += 1
    for letter, count in letter_count.items():
        if count ==1:
            return letter
    return None


# return [k for k,v in Counter.items if v == 1]


# import re
# pattern = re.compile(r'^w{2,}')
# match = pattern.match('teeter')
# print(match)