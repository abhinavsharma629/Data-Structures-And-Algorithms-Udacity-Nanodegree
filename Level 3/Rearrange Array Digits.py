# Python program for implementation of Radix Sort

input_list=[]

#------------------------INPLACE SORTING ALGORITHM----------------------------------------

# A function to do counting sort of arr[] according to
# the digit represented by exp.

def countingSort(arr, exp1):
    n = len(arr)

    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i]//exp1)
        count[ (index)%10 ] += 1

    for i in range(1,10):
        count[i] += count[i-1]

    # Build the output array
    i = n-1
    while i>=0:
        index = (arr[i]//exp1)
        output[ count[ (index)%10 ] - 1] = arr[i]
        count[ (index)%10 ] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i]


# Method to do Radix Sort
def radixSort(arr):

    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1/exp > 0:
        countingSort(arr,exp)
        exp *= 10


def rearrange_digits(input_list1):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    input_list=input_list1
    if(len(input_list)==0):
        return []
    elif(len(input_list)==1):
        return input_list

    radixSort(input_list)

    output_list=[]
    c=len(input_list)-1
    right=""
    left=""

    while(c>=0):
        right+=str(input_list[c])
        c-=1
        if(c>=0):
            left+=str(input_list[c])
            c-=1

    output_list.append((int)(right))
    output_list.append((int)(left))
    return output_list



def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[], []])
test_function([[4], [4]])
test_function([[1, 2], [2, 1]])
test_function([[4, 6, 2], [62, 4]])
