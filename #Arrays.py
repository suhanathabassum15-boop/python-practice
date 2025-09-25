#Arrays 
                                   
#Creating int array
import array
numbers = array.array('i',[1, 2, 3 , 4, 5,])
print(numbers) 

#Create float array
floats = array.array('f' ,[1.1,2.2,3.3])
print(floats)

#indexing
nums = array.array('i' , [10, 20 , 30 ,40])
print(nums[0])
print(nums[2])

#Slicing 
nums = array.array('i',[10,20,30,40,50 ])
print(nums[1:4])
print(nums[::-1])

#Adding elements
nums = array.array('i',[1, 2, 3])
nums.append(4)
print(nums)

#insert
nums.insert(1,10)
print(nums)

#Removing
nums.remove(10)
print(nums)

#Delete
del nums[0]
print(nums)
