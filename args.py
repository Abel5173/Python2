# # *args
# Python allows you to have functions with varying numbers of arguments.
# Using *args as a function parameter enables you to pass an arbitrary number of arguments to that function. The arguments are then accessible as 
# the tuple args in the body of the function.

# def function(named_arg, *args):
#     print(named_arg)
#     print(args)

# function(1,2,3,4,5,6)

# **kwargs
# **kwargs (standing for keyword arguments) allows 
# you to handle named arguments that you have not 
# defined in advance.
# The keyword arguments return a dictionary in which 
# the keys are the argument names, and the values are 
# the argument values.

# def my_func(x, y=7, *args, **kargs):
#     print(kargs)

# my_func(2,3,4,5,6,a=7,b=8)

def convert(num):
    if num == 0:
        return 0
    return (num%2 + 10 * convert(num//2))

a = int(input())
print(convert(a))