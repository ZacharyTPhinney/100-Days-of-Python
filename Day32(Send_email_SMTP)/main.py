##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 



##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.





# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.

import datetime as dt
import smtplib
import random
import pandas
my_email = "zacharytphinney@gmail.com"
password = "hnofqulhhrllryeb"
DATA= pandas.read_csv("birthdays.csv")
df = pandas.DataFrame(data=DATA)
df = df.to_dict
now = dt.datetime.now()
day_of_week = now.weekday()
month = now.month
day = now.day

DATA= DATA.to_dict("series")

birthdays = pandas.read_csv("birthdays.csv")
#
lines = birthdays.to_dict()
print(day)
# for i in range(1,len(birthdays)):
line = {1,2,3,4}

for day in lines["day"]:
    for month in lines["month"]:
        if lines["day"][day] == now.day and lines["month"][month] == now.month:

            print(lines["day"][day],lines["name"][day])

            for i in range(1,4):
                with open(f"letter_templates/letter_{i}.txt") as text:
                    read = text.read()
                    new = read.replace("[NAME]",(lines["name"][day]))
                    print(new)
            connection = smtplib.SMTP('smtp.gmail.com')
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
            from_addr=my_email,
            to_addrs="zacharytphinney@protonmail.com",
            msg=f"Subject:Happy Birthday \n\n{new}"
            )
            connection.close()
            print(new)



# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }



#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)





# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
