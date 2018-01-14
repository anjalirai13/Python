# a basic function
print "Welcome to Python Function argument type examples"
def printStr(str):
	print "str is: ", str       # it will print the string
	return;

printStr("This is an example for a basic function")
print "\n\n"

# an example of keyword arguments function
print "This is an example for a keyword argument function"
def printinfo(name, age):
	print "name is: ", name, "  and age is: ", age
	return;

printinfo("Anjali", "26")
printinfo(age = "26", name =  "Anjali")
print "\n\n"

# a function with default argument, if arguments is not specified
# while calling function default value is assigned
print "This is an example for a default argument function"
def printinfo(name, age = "35"):
	print "name is ", name, "age is ", age
	return;

printinfo("Neha", "26")
printinfo("Sameeksha")
print "\n\n"

# variable length arguments function
print "This is an example for a variable length argument function"
def variableLengthArguments (arg1, *vartuple):
	print "arg1 is ", arg1
	for var in vartuple:
		print var
	return;

variableLengthArguments (10)
variableLengthArguments (70, 60, 50)
print "\n\n"

# Anonymous functions(lambda):- functions not defined using def keyword
print "This is an example for a lambda(Anonymous function)"
lambdaSum = lambda arg1, arg2 : arg1 + arg2
print "value of total is ", lambdaSum( 10, 20 )