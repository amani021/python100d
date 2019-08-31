#-------- DAY 12 "exercise" --------
#Assign value to variables
x, y, mainText = 5, 7, "Please, I want {} sandwishies and {} donutes"
#Use some methods
text1 = mainText.replace('I', 'we')
text2 = text1.format(x, y)
#In this point, we can use another method to change each 'a' to 'A'
#BUT we didn't take it yet, so I use replace method
text3 = text2.replace('a', 'A')
#Print the final text
print(text3)
