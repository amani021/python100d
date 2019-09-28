#-------- DAY 40 "exercise2" --------
list, result = [-4, -6, -5, -1, 2, 3, 7, 9, 88], []
print('The main list is:\n', list)
positive_num = lambda num: num > 0
for x in list:
    if positive_num(x):
        result.append(x)
print('The positive numbers in the list are:\n', result)
