#Q1
def mul_numbers(a, b):
    print("mul of a n b=",a*b)
    return
a = int(input("Enter A Number:"))
b = int(input("Enter A Number:"))
mul_numbers(a,b)
#Q2
def even_or_odd(num):
    if num%2==0:
        return("even")
    else:
        return("odd")
num = int(input("Enter A Number:"))
print("The Num Is,",even_or_odd(num))

#Q3
def fact(num):
    fact = 1
    for i in range(1,1+num):
        fact*=i
    return fact
num = int(input("Enter A Number:"))
print("The Factorial of",num, "is",fact(num) )

#Q4
def largest_of_three(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
a = int(input("Enter A Number:"))
b = int(input("Enter A Number:"))
c = int(input("Enter A Number:"))
print("The largest number is ," ,largest_of_three(a,b,c))

#Q5
def reverse_str(str):
    return str[::-1]
txt = input("Enter a text:")
print("Reverse string is, ",reverse_str(txt))

#Q6
def count_vowels(str):
    vowels ="aeiouAEIOU"
    count=0
    for char in str:
        if char in vowels:
            count+=1
    return count
txt = input("Enter a text:")
print("Vowels:",count_vowels(str))


     



