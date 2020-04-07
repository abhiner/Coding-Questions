from datetime import datetime
enter_date = input('Enter a date (year,month,day)')
year, month, day = map(int, enter_date.split(','))
date = datetime(year, month, day)
week = date.isocalendar()[1]
print(week)
