#!/usr/bin/python

total = 0;   # global variable

# Function definition
def addition(arg1, arg2):
	total = arg1 + arg2;
	print "Inside the function local total : ", total    # addition of arg1 + arg2
	return total;

addition(30, 20);
print "Outside the function total is : ", total    # value is 0