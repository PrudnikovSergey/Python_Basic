import sys
import datetime as dt


date_str = '22.12.1987'
b_date = dt.datetime.strptime(date_str, '%d.%m.%Y')
now = dt.datetime.now()

print(b_date.timestamp())

# print(now.year - b_date.year)

delta = dt.timedelta(days=15)
# print(b_date + delta)

new_date = now + delta
print(new_date.strftime('%d %b %Y %H:%M'))

int_date = 1671188120000
print(dt.datetime.fromtimestamp(int_date / 1000))
