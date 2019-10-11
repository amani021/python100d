#-------- DAY 53 "exercise" --------
import Calculate as cal
import datetime

x = datetime.datetime.now()
print(x.strftime('%c'), '\n---------------------')
print('We have the basic operations wich are: +, -, * and /')
print('Examples for each one:')
print('1 + 8 =', cal.add(1, 8))
print('4 - 2 =', cal.subtract(4, 2))
print('6 * 6 =', cal.multiply(6, 6))
print('8 / 2 =', cal.divide(8, 2))
