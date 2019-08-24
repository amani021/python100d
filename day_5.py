#-------- DAY 5 "exercise" --------
x, y, z = 'apple', 'orange', 'limon' #Assign value to multiple variables
basket = x + y + z
print("The main text is:\n" + basket)
n = 4
text = '' #Assign an empty string
print("---------------------\n* After split the text using len() function by 4:")
for i in range(0, len(basket), n):
    #[start index : last index]
    text += basket[i:i+n] + ' '
print(text)
print("* Another way to split by using a list of length:")
#if you need to split a string with different length
#you can write it as a list
m = [5, 6, 5]
print(", ".join([basket[0:5], basket[5:11], basket[11:16]])) #join function to concatenate multi-string together
