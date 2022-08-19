# import re

# pattern = r"spam"
# if re.match(pattern,'eggspamsausaespam'):
#     print('Match')
# else:
#     print('No match')
# if re.search(pattern, 'eggspamsausaespam'):
#     print('Match')
# else:
#     print('No match')
# print(re.findall(pattern, 'eggspamsausaespam'))
# #-------------->Search<-----------------
# import re 
# p = r'pam'

# match = re.search(p, 'eggspamsuasage')
# if match:
#     print(match.group())
#     print(match.start())
#     print(match.end())
#     print(match.span())

# import re
# p = r'test'
# match = re.search(p, 'some test')
# print(match.start())
# print(match.end())

# # ----------------> Search & Replace <---------------
# import re 
# str = 'My name is David. Hi David.'
# p = r'David'
# newstr = re.sub(p, 'Amy', str, count=1)
# print(newstr)

# import re 
# num = '91934956789'
# p = r'9'
# num = re.sub(p, '0', num, count=2)
# print(num)

# # -------------> Metacharacters <-------------------
# import re 
# p = r'gr.y'
# if re.match(p, 'grey'):
#     print('Match 1')
# if re.match(p, 'gray'):
#     print('Match 2')
# if re.match(p, 'griy'):
#     print('Match 3')

# import re
# pattern = r"^gr.y$"
# if re.match(pattern, 'gray'):
#     print('Match 1')
# if re.match(pattern, 'gray'):
#     print('Match 2')
# if re.match(pattern, 'stingray'):
#     print('Match 3')
##--------------------> Character Classes <----------------------
# import re
# pattern = r'[aeiou]'
# if re.search(pattern, 'grey'):
#     print('Match 1')
# if re.search(pattern, 'qwertyuiop'):
#     print('Match 2')
# if re.search(pattern, 'rhythm myths'):
#     print('Match 3')

# import re 
# p = r'[A-Z][A-Z][0-9]'
# if re.search(p, 'LS8'):
#     print('Match 1')
# if re.search(p, 'E3'):
#     print('Match 2')
# if re.search(p, '1ab'):
#     print('Match 3')

# #-----------> invert <--------------
# import re
# p = r'[^A-Z]'
# if re.search(p, 'this is all quite'):
#     print('Match 1')
# if re.search(p, 'Abcdefg123'):
#     print('Match 2')
# if re.search(p, 'THISISALLSHOUTING'):
#     print('Match 3')

# import re 
# pattern = r'egg(spam)*'
# if re.match(pattern, 'egg'):
#     print('Match 1')

# if re.match(pattern, 'eggspamspamegg'):
#     print('Match 2')

# if re.match(pattern, 'spam'):
#     print('Match 3')

# import re 
# pattern = r'a(bc)(de)(f(g)h)i'
# match = re.match(pattern, 'abcdefghijklmnop')
# if match:
#     print(match.group())
#     print(match.group(0))
#     print(match.group(1))
#     print(match.group(2))
#     print(match.group())
# #-----------------> Groups <---------------
# from ast import MatchValue
# import re 
# pattern = r'(?P<first>abc)(?:def)(ghi)'
# match = re.match(pattern, 'abcdefghi')
# if match:
#     print(match.group('first'))
#     print(match.group())
# #-----------------> Metacharacters <---------------
# import re 
# pattern = r'gr(a|e)y'
# match = re.match(pattern, 'gray')
# if match:
#     print('Match 1')
# match = re.match(pattern, 'grey')
# if match:
#     print('match 2')
# match = re.match(pattern, 'griy')
# if match:
#     print('Match 3')
# #-----------------> Match <---------------
# import re 
# p = r'spam'
# if re.match(p, 'abel'):
#     print('Match')
# else:
#     print('No match')

# from itertools import count
# for i in count(3):
#     print(i)
#     if i > 20:
#         break

# def print_even(test_list):
# 	for i in test_list:
# 		if i % 2 == 0:
# 			return i

# test_list = [1, 4, 5, 6, 7]

# print("The original list is : " + str(test_list))

# print("The even numbers in list are : ", end=" ")
# for j in print_even(test_list):
# 	print(j, end=" ")

# def func(**kwargs):
#   print(kwargs["zero"])

# func(a = 0, zero = 8)
# #----------------> Dictionaries <-------------
# nums = {
#   1: 'one',
#   2: 'two',
#   3: 'three'
# }
# print(1 in nums)
# print('three' in nums)
# print(4 not in nums)

# pairs = {
#   1:'apple',
#   'orange': [2,3,4],
#   True: False,
#   12: 'True',
# }
# print(pairs.get('orange'))
# print(pairs.get(7, 42))
# print(pairs.get(12345, 'not found'))

# nums = (55,44,33,22)
# print(min(nums[:2]), abs(-42))

# text = input()
# dict = {}
# #your code goes here
# for i in text:
#     dict.update({i: text.count(i)}) 
# print(dict) 
# import numpy as np
# a =np.arange(100)
# print(a)
# def apply_twice(func, arg):
#     return func(func(arg))
# def add_five(x):
#     return x + 5
# print(apply_twice(add_five, 10))
# def my_func(func, arg):
#     return func(arg)
# print(my_func(lambda x: 2*x*x, 5))
##-----------> map <------------
# def add_five(x):
#     return x+5
# nums = [11, 22, 33, 44, 55]
# result=list(map(add_five, nums))
# print(result)
# result=list(map(lambda x: x*5, nums))
# print(result)

##-------> filter <----------
# nums = [11, 22, 33, 44, 55]
# res = list(filter(lambda x: x%2!=0, nums))
# print(res)
 
##---------->Generators<---------- 
# Generators are a type of iterable, like listsor tuples.
# Unlike lists, they don't allow indexing with arbitray
# indices, but they can still be iterated through with 'for' loops.
# They can be created using functions and the 'yield'
# statement.
# def countdown():
#    i = 5
#    while i>0:
#       yield i 
#       i -= 1
# for i in countdown():
#     print(i)
def numbers(x):
    for i in range(x):
        if i%2 == 0:
            yield i

print(list(numbers(11)))