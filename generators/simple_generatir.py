"""
Generator in python is a special type of iterator
that allows you to iterate over sequence of values
without storing them in a memory

Generators are more efficient
they produce values only when they needed
generators are make it easier to work with large datasets

"""

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))

#Using Generators with Loops




