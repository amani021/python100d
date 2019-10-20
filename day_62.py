#-------- DAY 62 "pip" --------
import camelcase

print("Lesson 62: PIP")
# 1. PIP is a package manager for python packages, or modules
# *** NOTE: python version 3.4 or later, PIP is included by default
#     otherwise, you will install it ***
# 2. To check if PIP is installed or not, and which version is, write 'pip --version' in your command line
#     to the location of python's script directory
# 3. Download a package writing 'pip install packageName'
# 4. Remove a package writing 'pip uninstall packageName'
# 5. To know all the packages you have in your system writing 'pip list'

c = camelcase.CamelCase()
txt = "lorem ipsum dolor sit amet"
print(c.hump(txt)) #Make capitalizes the first letter of each word
