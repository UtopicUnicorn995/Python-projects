##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import datetime as dt
import smtplib
import pandas
import random

my_email = "christianpy123@gmail.com"
password = "sdclnpccssmamibh"
now = dt.datetime.now()

with open('birthdays.csv') as file:
    reader = pandas.read_csv(file).to_dict('records')
    for item in reader:
        if item["month"] == now.month and item["day"] == now.day:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                with open(f'./letter_templates/letter_{random.randrange(2) + 1}.txt') as letters:
                    letter = letters.read()
                    new_letter = letter.replace("[NAME]", str(item["name"]))
                connection = smtplib.SMTP("smtp.gmail.com", 587)
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=item["email"], msg=f"Subject:Happy Birthday!\n\n{new_letter}")
