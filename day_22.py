#-------- DAY 22 "dictionaries 1" --------
# 1. Create a dictionary like a set if it's an empty
# 2. Assign to the dictionary, the syntax is: {keys:values}
# 3. Access the dictionary values by:
#     a. Referring to the keys which is almost like the indexes
#     b. Or using get() method
# 4. Print keys/values:
#     a. Using for loop:
#         - Print just keys if you used the usual way
#         - Print values:
#             >> Write print(object[variable]) inside for loop
#             >> Or just write for variable in object.values():
#         - Print both keys & values:
#             >> Write for var1, var2 in object.items():
#     b. Or just using print()
# 5. Change a value
text = "Lesson {}: Dictionaries 1"
dic1, dic2 = {1:22}, {'   English      ':'           Malay', '----------------------':'----------------------'}
dic3 = {
'Good evening       ':'Selamat pagi',
'How are you?       ':'Apa khabar?',
'What is your name? ':'Apa nama awak?',
'What do you do?    ':'Apa yang awak buat?'
}
print(text.format(dic1.get(1)))
print('YES YES YES ^__^/\nToday is my day to learn you a little bit of a language ;D')
print('Check the table in below and hope you enjoy\n')
dic3['Good evening       '] = 'Selamat petang'
for x, y in dic2.items():
    print(x + y)
for var1, var2 in dic3.items():
    print(var1 + '  |   ' + var2)
