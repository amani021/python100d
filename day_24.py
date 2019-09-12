#-------- DAY 24 "dictionaries 3" --------
# 11. Methods:
#     c. copy(): make a copy of a dictionary
#     d. dict(): also to make a copy of a dictionary or make a new dictionary
# 12. Make nested dictionaries
dic1 = dict(day=24)
dic2 = dic1.copy()
#fromkeys(,): takes 2 arguments & it'll return a new dictionary
dic3 = dict.fromkeys({'French', 'Malay', 'English', 'Spain'}, 'language')
text = "Lesson {}: Dictionaries 3"
dic1.clear()
dic2.update({'lesson':{24, 'dictionaries'}}) #Adding a new nested dictionaries
dic2.setdefault('part') #Adding a new key with a value 'None'
print(text.format(dic2.setdefault('day')))
print('3 dictionaries for today:\nDic1 = ', dic1, '\nDic2 = ', dic2, '\nDic3 = ', dic3)
#keys(): returns a list containing the dictionary's keys
# print(dic3.keys())
