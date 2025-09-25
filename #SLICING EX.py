 #SLICING EX
fruits = ("aaple" , "banana" , "mango" , "grapes" , "orange")
#Slicing idx feom 1 to 3
print(fruits[1:3])
#Slicing from begining up to idx3
print(fruits[:3])
#slicing from idx 2 to end
print(fruits[2:])
#step slicing
print(fruits[::2]) 
#Reverse tuple
print(fruits[::-1])


#COUNT METHOD
num = (1, 2, 3 , 2 , 1, 2)
count_2 = num.count(2)
print(num[1:len(num)])#it prints what are the values(val) 
print(count_2) #it prints how many were there(number)


#IDX METHOD
fruits  = ("apple" , "banana" , "mango" , "apple")
idx_apple = fruits.index("apple")
print(idx_apple)