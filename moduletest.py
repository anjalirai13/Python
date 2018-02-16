def module_test_fib_func (n):
	a, b = 0, 1
	while b < n:
		print b,
		a, b = b, a+b

def module_print_function ():
	print "Hi this is module : ", __name__