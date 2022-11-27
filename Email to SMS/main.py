import smtplib

my_email = "my_email@gmail.com"
password = "password for applications"
my_phone = "my phone number email"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=my_phone, msg="Subject: None\n\nNone")
