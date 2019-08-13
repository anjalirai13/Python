import moduletest
moduletest.module_test_fib_func(50)

# print moduletest.module_test_fib_func.__name__		# Ans : module_test_fib_func
# print __name__ 			# Ans : __main__

print "\n"
# Getting the argument from user and call the function
if __name__ == "__main__":
    import sys
    moduletest.module_test_fib_func(int(sys.argv[1]))