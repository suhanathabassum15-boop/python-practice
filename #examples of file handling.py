#examples
#Handling Zero Division Error
try:
    x = 10/0
except ZeroDivisionError:
    print("X cannot divide by zero")
finally:
    print("Program Ended")
#Multiple Exceptions
try:
    num = int("abc")
    result = 10/0
except ValueError:
    print("X Invalid number")
except ZeroDivisionError:
    print("X cannot divide by zero")
finally:
    print("Done")
#Catch Any Exception
try:
    f = open("data.txt")
except Exception as e:
    print("Error:", e)
finally:
    print("File handling attempted")