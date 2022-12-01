import random

import smtplib

email = " "
password = " "
phone = " "

quotes_list = []
with open("quotes.txt") as file:

    for line in file:
        quotes_list.append(line)

quote = random.choice(quotes_list)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs=phone, msg=f"Subject: Motivational quote \n{quote}")
