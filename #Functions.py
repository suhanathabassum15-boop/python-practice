#Functions
def greet():
    print("Welocome to Py function!")
greet()

def greet_user(name):
    print("Hello,",name)
greet_user("Shonu")

def sum(a, b ,c):
    print("SUM = ",a+b+c)
sum(2007, 10,15)

def introduce(name, age,town):
    print(f"My Name is {name}\nI am {age}years old\nAnd I am from {town}")
introduce(name="Suhana",age=17,town="Nalgonda")
introduce(name="Thabassum",age=17,town="NLG")

def greet(name="Guest"):
    print("Hello,",name)
greet()
greet("Thabasssum")
