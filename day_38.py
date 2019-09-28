#-------- DAY 38 "arrays2" --------
print("Lesson 38: Arrays 2")
# 6. Print all items of the array using for loop
# 7. Python has a set of built-in methods that you can use on lists/arrays, such as:
#     a. append(): for add an item to the end of the array
#     b. remove(): to remove an item from an array
#     c. pop(): also to remove an item from an array BUT the specified index or if you don't write an index it'll remove the last one
arr = ['orange', 'mango', 'apple', 'strawberry', 'mango']
arr.remove('mango')
arr.append('banana')
arr.pop()
print('I like to eat:')
for x in arr:
    print(' ', x)
