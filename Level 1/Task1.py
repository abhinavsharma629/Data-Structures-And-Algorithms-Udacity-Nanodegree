"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

# Using Sets for neglecting duplicates
final_list=set()

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    #Appending to set in not present
    for i in texts:
    	final_list.add(i[0])
    	final_list.add(i[1])


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    #Adding to set in not present
    for i in calls:
    	final_list.add(i[0])
    	final_list.add(i[1])


print("There are {} different telephone numbers in the records.".format(len(final_list)))

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
