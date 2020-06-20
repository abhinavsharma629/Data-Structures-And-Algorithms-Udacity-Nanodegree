"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)


def checkCaller(phone_no):
	if(len(phone_no.split("("))>0):
		return True


def checkCaller(phone_no):
	if(phone_no[0]=="("):
		return True if phone_no.split("(")[1].split(")")[0]=="080" else False

	return False

def getReceiver(phone_no):
	# if telephone no
	if(phone_no[0]=="("):
		return phone_no.split("(")[1].split(")")[0]
	
	# if mobile no
	elif(len(phone_no.split(" "))>0):
		return phone_no.split(" ")[0][0:4]
	
	# if telemarketers no
	else:
		return phone_no.split("140")[1]
	

list_of_codes=set([])
calls_total=0
call_and_receive_total=0


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for call in calls:
        # check if caller from banglore
    	isCallerFromBanglore=checkCaller(call[0])
    	getReceiverNo=getReceiver(call[1])

    	# if caller from banglore
    	if(isCallerFromBanglore):
    		list_of_codes.add(getReceiverNo)

            # check if receiver from banglore
    		isReceiverFromBanglore=checkCaller(call[1])
    		if(isReceiverFromBanglore):
                # inc banglore -> banglore calls count
    			call_and_receive_total+=1

            # inc total banglore calls count
    		calls_total+=1

    print("The numbers called by people in Bangalore have codes:")

    list_of_codes=sorted(list_of_codes)
    for list_code in list_of_codes:
    	print(list_code)

    percent=round((float)((call_and_receive_total/calls_total))*100,2)
    print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percent))


"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
