#-------- DAY 25 & 26 "exercise" --------
set = {1, 3, 5, 7, 8}
dic = {'name       ':' pigeon', 'type       ':' bird', 'skin cover ':' feathers'}
print('The main set & dictionary are:')
print('Set = ', set, '\nDictionary =')
for var1, var2 in dic.items():
    print('  ', var1, '|', var2)
set.update([4, 8, 12])
print('---------------------\nAfter task 1 is done:')
print("Set = ", set, "\nThe type's value in the dictionary is:", dic.get('type       '))
set.discard(8)
dic['skin cover '] = ' plastic'
print('---------------------\nAfter task 2 is done:')
print('Set = ', set, '\nDictionary =')
for var1, var2 in dic.items():
    print('  ', var1, '|', var2)
set.clear()
dic.clear()
print('---------------------\nAt the end, what do you think about emptying all data?',
'\nTo close this week and prepare fot the next lessons XD!')
print(set, ' &  dic', dic)
