"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
	reader = csv.reader(f)
	texts = list(reader)[0]
	print("First record of texts, {} texts {} at time {}".format(texts[0], texts[1], texts[2]))


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    calls=calls[len(calls)-1]
    print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(calls[0], calls[1], calls[2], calls[3]))


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

