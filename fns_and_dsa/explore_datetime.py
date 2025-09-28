# explore_datetime.py

import datetime

current = datetime.datetime.now()
print("Current date and time:", current)

days = int(input("Enter number of days to add: "))
future = current + datetime.timedelta(days=days)
print("Future date:", future.date())
