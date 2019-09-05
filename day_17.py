#-------- DAY 17 "tuples 2" --------
# 7. Use in keyword with if condition as we used with lists
# 8. Repeat item/s in a tuple using *
# 9. Concatenate tuples together by +
# 10. Methods:
#     a. len(): as we knew it's for count the number of length, we used with strings & lists, now with tuples
#     b. tuple(): makes a tuple
tuple1, tuple2, tuple3, list = (3, 4, 5, 6), tuple(('Good', 'Good', 'Bad'))*2, ('s')*2, [3, 4, 5, 6, "A", "B"]
tuple1 += (1, 2, 3)
tuple4 = tuple(list) #Change from a list to a tuple
#index() returns an index number of an element & count() returns how much the element appear in the tuple
print("Le" + str(tuple3) + "on 1" + str(len(tuple4)+tuple1.index(4)) + ": Tuples " + str(tuple2.count('Good')-tuple2.count('Bad')))
print('Tuple1 = ' + str(tuple4))
print('Tuple2 = ' + str(tuple1))
if 'A' in tuple4:
    print("Yes, 'A' is in the tuple1")
