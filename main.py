import datetime as dt
import smtplib
import calendar
import random
'''To protect private credentials, sensitive information has been stored on my personal laptop and only the necessary code is shared.'''
from secrets import *

# random quotes
quotes = open("quotes.txt").read().splitlines()
quotes = random.choice(quotes)
print(quotes)

# Date code
today = dt.datetime.now()
day_of_week = today.date()
day = calendar.day_name[day_of_week.weekday()]
# print(day)

if day=="Saturday":
    # location of smtp provider. It differs with different email providers.
    with smtplib.SMTP("smtp.gmail.com") as connection:
    # secures connection
        connection.starttls()
        # login
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
        to_addrs=send_to_address,
        msg=f'Subject: Saturday Motivation\n\n{quotes}'
                             )
else:
    print(f"Today is {day}")
