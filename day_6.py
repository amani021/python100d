#-------- DAY 6 "casting" --------
print("Lesson 6: Casting")
print("Python has something called 'Casting' changing from type to other type!")
print("---------------------\nFor example:")
print("In the 3rd lesson before, we talked about how to concatenate two things together BUT they should be in the same type")
print("Now, you can concatenate string with number!")
print("Using constructor functions: 1- int()    2- float()    3- str()")
print("*** NOTE: if you want to change from string to int or float, it should only containing a number!! ***")
print("\nEg.1: int()")
a, b, c = int(7), int(-2.4), int('8')
print(a) #You can ignore using int() function
print(b)
print(c)
#print(int('It is 10')) #It will be an error
print("\nEg.2: float()")
print(float(3))
print(float(13.2)) #You can ignore using float() function
print(float('8'))
print(float('-3.54'))
#print(float('It is 9.2')) #It will be an error
print("\nEg.3: str()")
#x = str('My fav number is ') #You can use it without str() function
print(str(8.5) + ', ' + 'My fav number is ' + str(22)) #You can use this in lesson 3 :)
