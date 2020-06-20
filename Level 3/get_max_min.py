import sys

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    mini=sys.maxsize
    maxi=0
    for i in range(0, len(ints)):
    	if(ints[i]>maxi):
    		maxi=ints[i]

    	if(ints[i]<mini):
    		mini=ints[i]

    return (mini,maxi)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((0, 0) == get_min_max([0,0])) else "Fail")
print ("Pass" if ((0, 1) == get_min_max([0,1])) else "Fail")
print ("Pass" if ((1, 2) == get_min_max([1,2])) else "Fail")
print ("Pass" if ((0, 5) == get_min_max([5,0])) else "Fail")