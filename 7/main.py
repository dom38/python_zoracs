# Dates are FUCKEN DUMB
import datetime
from datetime import datetime as dateandtime, date, time, timezone, timedelta

# Print the date and time now

print(datetime.datetime.now().strftime("%x"))

print(dateandtime.now())

# Print JUST today's date

print(date.today())


# Print x days into the future

print(dateandtime.now() + timedelta(days=7))

# Print x minutes ago

def my_function(number):
    print(dateandtime.now() - timedelta(minutes=number))

my_function(5)
my_function(10)
my_function(10000000)