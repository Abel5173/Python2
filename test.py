# from itertools import count

# for i in count(3):
#     print(i)
#     if i >= 11:
#         break
# from itertools import accumulate, takewhile

# nums=list(accumulate(range(8)))
# print(nums)
# print(list(takewhile(lambda x: x<=6, nums)))

# from itertools import product, permutations

# letters = ('A', 'B')
# print(list(product(letters, range(2))))
# print(list(permutations(letters)))

# num = int(input())

# def fib(n):
#     if n<=2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)

# def fibonacci(n):
# 	#complete the recursive function
#     for i in range(n):
#         if i <= 1:
#             print(i)
#         else:
#             print(fib(i))

# # fibonacci(num)
# class Vector2D:
#     def __init__(self, x, y):
#       self.x = x
#       self.y = y
#     def __add__(self, other):
#         return Vector2D(self.x+other.x, self.y+other.y)

def get_input():
  command = input(": ").split()
  verb_word = command[0]
  if verb_word in verb_dict:
    verb = verb_dict[verb_word]
  else:
    print("Unknown verb {}". format(verb_word))
    return

  if len(command) >= 2:
    noun_word = command[1]
    print (verb(noun_word))
  else:
    print(verb("nothing"))

def say(noun):
  return 'You said "{}"'.format(noun)

verb_dict = {
  "say": say,
}

while True:
  get_input()

  class GameObject:
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name + "\n" + self.desc

class Goblin(GameObject):
  class_name = "goblin"
  desc = "A foul creature"

goblin = Goblin("Gobbly")

def examine(noun):
  if noun in GameObject.objects:
    return GameObject.objects[noun].get_desc()
  else:
    return "There is no {} here.".format(noun)

verb_dict = {
  "say": say,
  "examine": examine,
}