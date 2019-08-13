Name = "Anjali"
def print_name():
	str1 = "name"
	Name = "Anjali Rai"
	print locals()

print Name
print_name()
print Name

def print_name_2():
	# global Name
	Name = "Anjali Rai"
	print globals()

print_name_2()
print Name