#TYPE CONVERSIONS
#List to tuple
my_list = [1 , 2, 3 , 4]
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))
#Tuple to list
my_tuple = (5 , 6, 7)
my_list = list(my_tuple)
print(my_list)
print(type(my_list))
#List to Set
my_list = [1 , 2, 2, 2, 3 ,3, 4]
my_set = set(my_list)
print(my_set)
print(type(my_set))
#Set to List
my_set = {10 , 20 , 30}
my_list = list(my_set)
print(my_list)
#Dictionary to List of keys
student = {'name':'John' , 'age':20 , 'grade':'A'}
key_list = list(student.keys())
print(key_list)
#Dictionary to List of values
student = {'name':'John' , 'age':20 , 'grade':'A'}
values_list = list(student.values())
print(values_list)
#Dictionary to List of items
student = {'name':'John', 'age':20 , 'grade':'A'}
values_list = list(student.items())
print(values_list)
