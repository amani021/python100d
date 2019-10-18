#-------- DAY 60 "exercise" --------
import json
import re

# 1. Convert from python object to JSON string
t = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
print('JSON string is:\n', json.dumps(t))
# 2. Search for 'data' word in the text with 2 ways
txt = 'data is the new oil'
x = re.search(r'\bd\w+', txt)
print("---------------------\nThe text is:", txt)
print("Find 'data' word from the text:\n", x.group())
print('', re.findall('data', txt))
