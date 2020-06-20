import math

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    l=0
    r=number

    while(l<=r):
    	mid=(l+r)//2

    	if(mid*mid>number):
    		r=mid-1
    	elif(mid*mid<number):
    		l=mid+1
    	else:
    		return mid
    		break

    return r

print ("Pass" if  ((math.floor(math.sqrt(9))) == sqrt(9)) else "Fail")
print ("Pass" if  ((math.floor(math.sqrt(0))) == sqrt(0)) else "Fail")
print ("Pass" if  ((math.floor(math.sqrt(16))) == sqrt(16)) else "Fail")
print ("Pass" if  ((math.floor(math.sqrt(1))) == sqrt(1)) else "Fail")
print ("Pass" if  ((math.floor(math.sqrt(27))) == sqrt(27)) else "Fail")
print ("Pass" if  ((math.floor(math.sqrt(2))) == sqrt(2)) else "Fail")
print ("Pass" if  ((math.floor(math.sqrt(3))) == sqrt(3)) else "Fail")
print ("Pass" if  ((math.floor(math.sqrt(100))) == sqrt(100)) else "Fail")
print ("Pass" if  ((math.floor(math.sqrt(10120343))) == sqrt(10120343)) else "Fail")
print ("Pass" if  ((math.floor(math.sqrt(27545445))) == sqrt(27545445)) else "Fail")