#higher order function
def square(x):
    return x*x
x = [1,2,3,4,5,6]
squared = set(map(square,x))
print(squared)

def is_even(x):
    return x%2==0
numbers = [1,2,3,4,5,6]
even_num = list(filter(is_even,numbers))

from functools import reduce
def add(x,y):
    return x+y
numbers = [1,2,3,4,5,6]
sum_num = reduce(add,numbers)
print(sum_num)


