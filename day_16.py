#-------- DAY 16 "tuples 1" --------
# 1. Create and assign to a tuple
# 2. Access the tuple items by referring to the index number
# 3. Print all items of the tuple using for loop
# 4. Change / Add / Remove an item value will can't use with tuples
# 5. Delete an object using del keyword
# 6. How to take some items from the tuple?
#We learned this way before in lesson 5, 7 & 14 BUT with strings & lists
#Now we will use it with tuples
#Write as ('red',) to distinguish from a simple variable
tuple1, tuple2 = ('Sep',), ('Tuples', 4, 19)
info = "Tuples are the same as lists except they are unchangeable!!"
for x in tuple1:
    print(x + ' ' + str(tuple2[1:3]))
print("Lesson 16: " + tuple2[0] + " 1\n" + info)
del tuple1
#print(tuple1) #Will make an error
