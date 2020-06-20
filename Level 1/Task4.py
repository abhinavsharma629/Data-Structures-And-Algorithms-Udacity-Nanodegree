"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


telemarketers={}
receivers=set()

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for call in calls:
        telemarketers[call[0]]=1

        # if already present in telemarketers dict then remove caller
        if(call[1] in telemarketers):
            del telemarketers[call[1]]

        receivers.add(call[1]) # add to the receivers list


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    # remove text senders and receivers from telemarketers list
    for text in texts:
        if(text[0] in telemarketers):
            del telemarketers[text[0]]
        if(text[1] in telemarketers):
            del telemarketers[text[1]]

# remove receivers from telemarketers list
for i in receivers:
    if(i in telemarketers):
        del telemarketers[i]

telemarketers=sorted(telemarketers.keys())

print("These numbers could be telemarketers: ")

for caller in telemarketers:
    print(caller)


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

