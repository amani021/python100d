#-------- DAY 18 & 19 "exercise" --------
list = ["java", "python", "swift"]
tuple = tuple(list)
print('List = ' + str(list) + '\nTuple = ' + str(tuple) + '\n---------------------')
#List Methods
list.extend(list[1:3]) #Add 'python' & 'swift' at the end of the list
list.remove('swift') #Remove 'swift' that appeared first
list.append('kotlin') #Add 'kotlin' at the end of the list
list.pop(2) #Remove 'python' that appeared secondly
print('The programming languages in my list are: ' + str(list) + ' and')
#Tuple Methods
if 'python' not in tuple:
    print("Yes, 'python' is not in the tuple")
else:
    print("Ofcourse, 'python' is in the tuple")
