#-------- DAY 51 "modules2" --------
# Python has several built-in modules
# 1. Re-naming a module using (as) keyword
import Module as m
import platform
# 2. Import part of a module
from Module import colors

print("Lesson 51: Modules 2")
m.txt('Amer')
print('Love', colors[3], 'things')
print('---------------------\nMy device uses', platform.system(), 'operating system')
print('And I use', platform.python_version(), 'version of python')
# 3. To list all the function or variable names in a module use dir() function,
# a built-in function
print(dir(platform))
