#How old are you?
from datetime import datetime

now = datetime.now()
print("Today: %04d/%02d/%02d" % (now.year, now.month, now.second))
input('Type in your birthday')
year = input('year: ')
month = input('month: ')
day = input('day: ')
if month > 'now.month':
    print('Your age is ', now.year - int(year))
elif month < 'now.month':
    print('Your age is ', now.year - int(year) + 1)