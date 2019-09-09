#-------- DAY 21 "sets 2" --------
# 8. Delete an object using del keyword
# 9. Methods:
#     a. len(): as we knew it's for count the number of length, we used with strings, lists & tuples, now with sets
#     b. remove(): removes an item from a set, if the item doesn't exist, it'll raise an error!!
#     c. discard(): also removes an item from a set BUT if the item doesn't exist, it'll NOT raise an error!!
#     d. pop(): returns an item removed from a set that is the last one BUT here with a set, you'll not know which item will remove!!
#     e. clear(): empties all items from a set
#     f. set(): makes a new set
text1, text2 = "Lesson {0}1: Sets {0}", "This is a wonderful lesson \\(^.^)/ BUT"
set1, set2, set3 = {'red', 'blue', 'purple', 'orange'}, {2, 1, 6, 1, 4}, set((2, 4, 'red', 'white'))
set4 = set1.copy()
#set3.remove('orange') #Will make an error
set2.discard(6)
print(text1.format(len(set2)-1))
print('Today color is: ' + str(set4.pop()))
print(text2 + "\nI think this is the biggest challenge for me to date '-.-")
print('The main sets are:')
print('Set1 = ' + str(set1) + '\nSet2 = ' + str(set2) + '\nSet3 = ' + str(set3) + '\nSet4 = ' + str(set4) + '\n---------------------')
print("Now you can see in below the set methods and thier results:")
#Returns a set containing set2 items that aren't in set3 => {1}
print('1- difference():\n     Set2 = ' + str(set2.difference(set3)) + '\n     Set3 = ' + str(set3))
set1.difference_update(set3) #Removes item/s only from set1 that appeared in set3 => 'red'
print('2- difference_update():\n     Set1 = ' + str(set1) + '\n     Set3 = ' + str(set3))
#Returns a set containing item/s that appeared in both sets => {2, 4}
print('3- intersection():\n     Set2 = ' + str(set2.intersection(set3)) + '\n     Set3 = ' + str(set3))
set2.intersection_update(set3) #Removes item/s from set2 that aren't in set3 => 1
print('4- intersection_update():\n     Set2 = ' + str(set2) + '\n     Set3 = ' + str(set3))
#Compare between sets if they have an intersection or not (have the same item/s or not)
print('5- isdisjoint():\n     Set1 is disjiont Set3?  ' + str(set1.isdisjoint(set3)))
set1.clear()
print('6- issubset():\n     Set1 is subset of Set2?  ' + str(set1.issubset(set2))) #Check if set1 is subset of set2 or not
#Check if set1 is a superset of set2 or not
print('7- issuperset():\n     Set1 is superset of Set2?  ' + str(set1.issuperset(set2)))
#*** NOTE: no matter if we reverse the variables!! ***
#Returns a set containing item/s that not present in both sets
print('8- symmetric_difference():\n     ' + str(set2.symmetric_difference(set3)))
set2.symmetric_difference_update(set3) #Returns set2 containing item/s that not present in both sets
print('9- symmetric_difference_update():\n     Set2 = ' + str(set2) + '\n     Set3 = ' + str(set3))
print('10- union():\n     Set4 U Set2 = ' + str(set4 | set2)) #Returns a set containing all items of sets
