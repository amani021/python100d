#-------- DAY 15 "lists 3" --------
print("Lesson 15: Lists 3")
# 11. Methods:
#     a. len(): as we knew it's for count the number of length, we used with strings and now we'll use it with lists
#     b. append(): for add an item to the end of the list
#     c. insert(,): also for add an item to the list BUT at the specified index
#     d. remove(): to remove an item from a list
#     e. pop(): also to remove an item from a list BUT the specified index or if you don't write an index it'll remove the last one
#     f. clear(): empties all items from a list
#     g. copy(): make a copy of a list
#     h. list(): also to make a copy of a list or make a new list
methods = ['len()', 'pop()', 'append()', 'remove()', 'pop()', 'reverse()', 'clear()', 'copy()', 'list()']
x = ['count()', 'extend()', 'index()', 'reverse()', 'sort()']
#index() returns an index number of an element & count() returns how much the element appear in the list
print('Good evening everybody :), I learned ' + str(len(methods)+methods.index('clear()')-methods.count('pop()')) + ' methods which are:')
methods.append('sort()')
methods.insert(3, 'insert()') #Adds it after append()
methods.remove('pop()') #Removes the first one
methods.pop() #Removes sort() that we added before
methods.pop(5) #Removes reverse()
methods.extend(x) #Adds x at the end of methods list
methods.reverse() #Reverses the order of the list
for x in methods:
    print('  ' + x)
methods.clear()
lists = methods.copy()
#list = list(methods)
myList = list(('Keyboard', 'Printer', 'Mouse', 'Speaker', 'Monitor')) #Make a new list
myList.sort() #Sorts the list
print('In previous lessons, you learned how to create a list x = ' + str(lists) + ' or an empty list')
print("Oh right! Yesterday I decided to buy " + str(myList) + " but\nwith that emergency problem, I couldn't buy :(\nSo, good bye. See you later.")
