#-------- DAY 20 "sets 1" --------
print("Lesson 20: Sets 1")
# 1. Create a set
# 2. Assign to the set
# 3. Can't access the set items by referring to the index number becuase it's unordered the items has no index
# 4. Print all items of the set using for loop
# 5. Use in keyword with if condition as we used with lists & tuples
# 6. Can't change an item value
# 7. Add item/s using:
#     a. add(): add one item to the set
#     b. update(): add more than one items to the set
set1, set2 = {5, 3, 'mouse', 'keyboard', 3}, {'unordered'}
print('Set is a collection which is:')
set1.update(['printer', 4, 4])
set2.add('unindexed')
for x in set2:
    print(x)
print('---------------------\nSet = ' + str(set1)) #Ignore duplecate items
if 'printer' in set1:
    print("Yes, 'printer' exists in the set")
else:
    print("The item doesn't exist!!")
