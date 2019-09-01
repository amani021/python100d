#-------- DAY 13 "lists 1" --------
print("Lesson 13: Lists 1")
# 1. Create a list
# 2. Assign to the list
# 3. Access the list items by referring to the index number
# 4. Print all items of the list using for loop
# 5. Change an item value
# 6. Delete an object or an element using del keyword
list1, list2 = [3.6, 7.204, 24.4], [-23, 43, 2.54, 90, -0.234, 342]
text = """List 1 = {}
List 2 = {}
These two lists we will change them with a little bit of steps through a story.\n---------------------"""
print(text.format(list1, list2))
stmt1 = """A short story says:
My name is Sara, I'm {} years old.
I want to tell you some numbers and then I wil make some change towards it.
The list is:"""
print(stmt1.format(list1[0] + list1[2]))
for num in list2:
    print(num)
stmt2 = """I don't like a number with negative sign, so I will change them.
Ummm.. also, float numbers I will remove it >.<
Finally :D, the two lists are:
List 1 = NameError: name 'list1' is not defined
List 2 = {}"""
list2[0], list2[4] = 32, 7 #The list will be: [32, 43, 2.54, 90, 7, 342]
del list2[2]
#del list1 #Will make an error
print(stmt2.format(list2))
