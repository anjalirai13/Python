#!/usr/bin/python

# an example of pass by reference changes made inside method
# will reflect outside
def changeme( mylist ):
	mylist.append([1, 2, 3, 4]);
	print "pass by reference my list inside function is ", mylist  # Ans: [10, 20, 30, 1, 2, 3, 4]
	return

mylist = [10, 20, 30]
changeme( mylist );
print "pass by reference mylist outside function is ", mylist # Ans: [10, 20, 30, 1, 2, 3, 4]

# an example of pass by value changes made inside method
# will not reflect outside
def changeme2( mylist ):
	mylist = ([1, 2, 3, 4]);
	print "pass by value my list inside function is ", mylist # Ans: [1, 2, 3, 4]
	return

mylist = [10, 20, 30]
changeme2( mylist );
print "pass by value mylist outside function is ", mylist # Ans: [10, 20, 30]
