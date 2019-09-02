#-------- DAY 14 "lists 2" --------
print("Lesson 14: Lists 2")
# 7. How to take some items from the list?
#We learned this way before in lesson 5 & 7 BUT with strings
#Now we will use it with lists
# 8. Use in keyword like in lesson 11 BUT with if condition
# 9. Repeat item/s in a list using *
# 10. Concatenate lists together by +
list1, list2 = ['Keyboard', 'Printer', 'Mouse', 'Speaker', 'Monitor'], ['Help!']*3
num1, num2 = [3.4, 23.6, 3.5], [5, 65, 13, 8]
text1 = "Hi guys, are you remember me? I'm Sara and today I have to buy new {} and "
text2 = """Oh! I'm hearing somebody screaming: {}
I'll go to him right away .. OMG!! What happened?
I'm seeing numbers {}
I don't understand what is the meaning?! I think it's..."""
print(text1.format(list1[1:4]))
if 'Keyboard' in list1:
    print("yes, 'Keyboard' too :)")
print(text2.format(list2, num1+num2))
