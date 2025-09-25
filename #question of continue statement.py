#question
list1 = [1 , 2 , 3 , 4 , 5 , 6 ,7 ,8]
for num in list1:
    if num % 3 == 0:
        print("skipping multiples of 3")
        continue
    print("Number :" , num) 


print("another question")

# scnd question
list2 = [1 , -2, 3 , 4, 5]
for num in list2:
    if num <0:
        print("skipping -ve numbers")
        continue
    print("Number:" , num)