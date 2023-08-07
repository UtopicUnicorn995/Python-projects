import smtplib 
import pandas
import random
import datetime as dt

now = dt.datetime.now()

my_email = "christianpy123@gmail.com"
password = "sdclnpccssmamibh"
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
with open("quotes.txt") as file:
    today_quote = random.choice(file.readlines())

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="christian.degulacion@gmail.com", msg=f"{days[now.weekday()]} motivation quote.\n\n{today_quote}")
