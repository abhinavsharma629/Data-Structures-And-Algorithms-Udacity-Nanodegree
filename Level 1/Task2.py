"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)


# # Can Create my own class for efficiency and clean code structure
# class CallLogs:
# 	number=""
# 	seconds=0
# 	date=""

# 	def __init__(self, phn_no, sec_of_talk, date):
# 		self.number=phn_no
# 		self.seconds=sec_of_talk
# 		self.date=date

# 	# Get Formatted Date
# 	def getDate(self):
# 		months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# 		mo,year=self.date.split("-")[0],self.date.split("-")[2].split(" ")[0]

# 		return "{} {}".format(months[(int)(mo)-1], year)



with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    max_call_log={}

    for i in calls:
    	# calculating max
    	if(i[0] in max_call_log):
    		max_call_log[i[0]]+=(int)(i[3])
    	else:
    		max_call_log[i[0]]=(int)(i[3])

    	if(i[1] in max_call_log):
    		max_call_log[i[1]]+=(int)(i[3])
    	else:
    		max_call_log[i[1]]=(int)(i[3])

    phone=""
    maxi=0
    for i,j in max_call_log.items():
    	if(j>maxi):
    		maxi=j
    		phone=i
    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(phone, maxi))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

