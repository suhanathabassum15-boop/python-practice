#QUESTIONS ON ARRAY

#1st question
import array
num = array.array('i',[1 ,2, 3, 4])
print(num[0])
print(num[-1]) 

#3rd question
num2 = array.array('i', [10,20,30,40,50,60,70 ])
slice_arr = arr[-5:2]
print("sliced array with negative indices",slice_arr)

#5th question
num3 = array.array('i' ,[5, 10, 15, 20 , 25 , 30] )
sli = num3[0:4]
total = 0
for i in sli:
    total += i
print("sum = ",total )

#6th question 
num4 = array.array('i',[1,2,3,4,5])
print(num4[::-1])

#2nd question
num5 = array.array('i',[2 , 4, 6 , 8 , 10 , 12] )
print(num5[2:5])

#4th question
num6 = array.array('i',[10 , 20 , 30 ,40 , 50])
print(num6[::2])








