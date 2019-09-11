#-------- DAY 23 "dictionaries 2" --------
# 6. Delete an object or an element using del keyword
# 7. Use in keyword with if condition as we used with lists, tuples & sets BUT it'll take just the keys to search them
# 8. Add item/s
# 9. Remove item/s using:
#     a. pop(): removes an item from a dictionary BUT the specified key
#         or if you don't write a key or it doesn't exist in the dictionary it'll raise an error!!
#     b. popitem(): removes the last inserted item & if the dictionary is empty it'll raise an error!!
# 11. Methods:
#     a. len(): as we knew it's for count the number of length, we used with strings, lists, tuples & sets
#     b. clear(): empties all items from a dictionary
dic1, dic2 = {1:11, 14:'morning', 17:'good'}, {'dictionary':2, 'list':3}
text = "Lesson {}: Dictionaries {}"
print(text.format(str(dic2['dictionary'])+str(dic2['list']), len(dic2))) #len() method counts key-value pairs
#Check if the key exists in the dictionary or not
if 1 in dic1:
    print("Yes, we are in 1 month (Muharram)")
dic2['string'] = 4
dic2['set'] = 7
dic2['tuple'] = 5
dic2.pop('string')
del dic1[14]
print('We have so far learned 4 types resembling some:')
for x in dic2:
    print('  ' + x)
