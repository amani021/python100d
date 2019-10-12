#-------- DAY 54 "extra exercise" --------
from datetime import date, timedelta

today = date.today()
yesterday = date.today() - timedelta(days=1)
tomorrow = date.today() + timedelta(days=1)

print(today, '\nExtra Exercise\n---------------------')
print('I finished writing a code of exercise on', yesterday)
print("And I'm excited for start a new week's lessons from tomorrow", tomorrow)
