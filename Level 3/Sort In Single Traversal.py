def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    countOfZero=0
    countOfOne=0
    
    for i in input_list:
        if(i==0):
            countOfZero+=1
        elif(i==1):
            countOfOne+=1

    two_cou=countOfOne+countOfZero
    one_cou=countOfZero
    zero_cou=0

    # setting zero
    for i in range(0,len(input_list)):
        if(input_list[i]==0):
            temp=input_list[zero_cou]
            input_list[zero_cou]=0
            input_list[i]=temp
            zero_cou+=1


    # setting one
    for i in range(0,len(input_list)):
        if(input_list[i]==1):
            temp=input_list[one_cou]
            input_list[one_cou]=1
            input_list[i]=temp
            one_cou+=1

    # setting two
    for i in range(0,len(input_list)):
        if(input_list[i]==2):
            temp=input_list[two_cou]
            input_list[two_cou]=2
            input_list[i]=temp
            two_cou+=1


    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    #print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])

test_function([])

test_function([2,2])
test_function([2])
test_function([2,2,2])

test_function([1,1])
test_function([1])
test_function([1,1,1])

test_function([0,0])
test_function([0])
test_function([0,0,0])

test_function([1, 2, 0])
test_function([0, 1, 2])
test_function([0, 2, 1])
test_function([2, 1, 0])

test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
