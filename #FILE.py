f = open("data.txt","w")
f.write("Hello , Python!\n")
f.close()

f = open("data.txt","w")
f.writelines(["line1\n" , "line2\n" , "line3\n"])
f.close()

f = open("data.txt","r")
print(f.read())
print(f.read(5))
f.close()

f = open("data.txt","r")
print(f.readline())
print(f.readline(5))
f.close() 

f = open("data.txt","r")
print(f.readline())
print(f.readline(5))
f.close() 

f = open("data.txt","r")
lines = f.readlines()
print(lines)
f.close() 


 
                                                                                                                                                                                                                                                        
                       










