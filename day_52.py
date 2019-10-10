#-------- DAY 52 "datetime" --------
import datetime

print("Lesson 52: Datetime")
x1 = datetime.datetime.now()
#strftime() method: to be display a date in different way
print('Today is', x1.strftime("%A"))
print('I write this code on', x1)
x2 = datetime.datetime(2020, 1, 1) #Create a date using the constructor of the datetime module
print('And I hope something amazing happens with the beginning of the year', x2)
